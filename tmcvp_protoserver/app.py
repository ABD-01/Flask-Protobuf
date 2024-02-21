import os
import sys
import logging
import uuid
from datetime import datetime

from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, FloatField

# sys.path.append("./TataMotorsCVP630")
# Adding TataMotorsCV630 to sys path
package_dir = os.path.abspath(os.path.dirname(__file__))
tata_motors_path = os.path.join(package_dir, 'TataMotorsCVP630')
if tata_motors_path not in sys.path:
    sys.path.append(tata_motors_path)
logging.root.setLevel(logging.DEBUG)

from google.protobuf.json_format import MessageToJson
import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2

from tmcvp_protoserver import utils

MQTT_BROKER = "test.mosquitto.org"
PORT_NO = 1883


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Replace with a secret key in production
app.config['MQTT_BROKER_URL'] = MQTT_BROKER
app.config['MQTT_BROKER_PORT'] = PORT_NO
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ' '
app.config['MQTT_REFRESH_TIME'] = 5.0  # refresh time in seconds
mqtt = Mqtt(app)
csrf = CSRFProtect(app)
socketio = SocketIO(app, async_mode='threading') 

CONTROL_RENDER_KW = dict(render_kw={"class":"form-control form-control-sm"})
SELECT_RENDER_KW = dict(render_kw={"class":"form-select form-select-sm"})
class CommandMessageForm(FlaskForm):
    """
    FlaskForm for creating a Command Message.

    Fields:
    - message_id (StringField): Unique identifier for the message.
    - correlation_id (StringField): Identifier for correlating messages.
    - vehicle_id (StringField): Identifier for the associated vehicle.
    - type (SelectField): Type of the message (e.g., command).
    - priority (StringField): Priority level of the message.
    - provisioning_state (SelectField): Provisioning state of the message.
    - version (StringField): Version of the message.
    - packet_status (SelectField): Status of the packet (e.g., Live).
    - subtype (SelectField): Subtype of the command message.

    Note for Future Upgrades:
    This form assumes that the fields message_id, correlation_id, vehicle_id, type,
    priority, provisioning_state, version, packet_status, and subtype are present
    in future proto versions of `CommandMessage` as in version TMCVP 6.3.
    If any of these headers change, the code needs to be modified.
    """
    message_id = StringField('Message ID', default=str(uuid.uuid4()), **CONTROL_RENDER_KW)
    correlation_id = StringField('Correlation ID', default='correlation-id', **CONTROL_RENDER_KW)
    vehicle_id = StringField('Vehicle ID', default='MH12VF1121', **CONTROL_RENDER_KW)
    type = SelectField('Type', choices=[(e.number, e.name) for e in tmcvp_common_pb2.eTcuMessageType.DESCRIPTOR.values], default=tmcvp_common_pb2.eTcuMessageType.command, coerce=int, **SELECT_RENDER_KW)
    priority = StringField('Priority', default='moderate', **CONTROL_RENDER_KW)
    provisioning_state = SelectField('Provisioning State', choices=[(e.number, e.name) for e in tmcvp_common_pb2.eProvisioningState.DESCRIPTOR.values], default=tmcvp_common_pb2.eProvisioningState.provisioned, coerce=int, **SELECT_RENDER_KW)
    version = StringField('Version', default='V6.3', **CONTROL_RENDER_KW)
    # time_stamp = StringField('Time Stamp', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), render_kw={'readonly': True})
    packet_status = SelectField('Packet Status', choices=[(e.number, e.name) for e in tmcvp_common_pb2.PacketStatus.DESCRIPTOR.values], default=tmcvp_common_pb2.PacketStatus.Live, coerce=int, **SELECT_RENDER_KW)
    subtype = SelectField('Subtype', choices=[(-1, "--- Select Subtype ---")]+[(e.number, e.name) for e in tmcvp_command_message_pb2.commandMessageSubType.DESCRIPTOR.values], coerce=int, **SELECT_RENDER_KW)


@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    # form = UserForm(request.form)
    form = CommandMessageForm(request.form)

    vinNo = session.get('vin_no', '')
    if vinNo:
        mqtt.subscribe("/device/" + vinNo + "/MQTTPROTOBUF/commandresponse")
    return render_template('index.html', form=form, vin_no=vinNo)

@app.route('/set_vin', methods=['POST'])
def set_vin():
    vin_no = request.form.get('vin_no')
    # Set VIN in the session
    session['vin_no'] = vin_no
    return jsonify({'status': 'success'})


@app.route('/get_additional_fields', methods=['POST'])
def get_additional_fields():
    subtype = request.form.get('subtype', -1)
    try:
        subtype = int(subtype)
        if subtype == -1:
            return jsonify({'additional_fields_html': ''})
    except:
        return jsonify({'additional_fields_html': ''})

    class DynamicForm(FlaskForm):
        pass

    payloadType = tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload"
    command_payload = getattr(tmcvp_command_pb2, payloadType)()

    form  = generateDynamicForm(command_payload, DynamicForm)(request.form)

    additional_fields_html = render_template('additional_fields.html', form=form)
    return jsonify({'additional_fields_html': additional_fields_html})
    
## now handling /send_command
@app.route('/send_command', methods=['POST'])
def send_command():
    subtype = request.form.get('subtype')
    try:
        subtype = int(subtype)
        if subtype == -1:
            return jsonify({'status': 'error', 'message': 'Invalid Subtype'})
    except:
        return jsonify({'status': 'error', 'message': 'Invalid Subtype'})

    command_message = generate_command_message(subtype, request.form)
    serialized_message = command_message.SerializeToString()

    CommandTopic = "/device/" + session.get('vin_no', '') + "/MQTTPROTOBUF/command"
    mqtt.publish(CommandTopic, serialized_message)
    socketio.emit('message', 'Command Sent: ' + CommandTopic)

    return jsonify({
        'status': 'success',
        'message': utils.MessageToDict(command_message),
        'messageHex': serialized_message.hex(' ').upper()
    })

NUM_REPEATED = 1
def generateDynamicForm(payload, formClass):
    """
    Generate a dynamic form based on the given payload and form class.

    Works almost same as :func:`utils.fill_message`.
    """
    for field_descriptor in payload.DESCRIPTOR.fields:
        field_name = field_descriptor.name
        field_type = field_descriptor.type

        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            values = field_descriptor.enum_type.values
            enum_choices = [(e.number, e.name) for e in values]
            setattr(formClass, field_name, SelectField(field_name, choices=enum_choices, coerce=int, **SELECT_RENDER_KW))
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = NUM_REPEATED
                for _ in range(num_repeated):
                    nested_payload = getattr(payload, field_descriptor.name).add()
                    generateDynamicForm(nested_payload, formClass)
            # IS NON REPEATED MESSAGE
            else:
                nested_payload = getattr(payload, field_descriptor.name)
                generateDynamicForm(nested_payload, formClass)
        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            num_repeated = NUM_REPEATED
            for _ in range(num_repeated):
                setattr(formClass, field_name, StringField(field_name, **CONTROL_RENDER_KW))
        else:
            if field_descriptor.type == field_descriptor.TYPE_DOUBLE or field_descriptor.type == field_descriptor.TYPE_FLOAT:
                setattr(formClass, field_name, FloatField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type in [field_descriptor.TYPE_INT32, field_descriptor.TYPE_INT64, field_descriptor.TYPE_UINT32, field_descriptor.TYPE_UINT64]:
                setattr(formClass, field_name, IntegerField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BOOL:
                setattr(formClass, field_name, BooleanField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_STRING:
                setattr(formClass, field_name, StringField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BYTES:
                setattr(formClass, field_name, StringField(field_name, **CONTROL_RENDER_KW))

    return formClass

def generate_command_message(subtype, form):
    """
    Generate a Command Message based on the provided subtype and form input.

    Parameters:
        subtype (int): The subtype of the command message corresponding to `enum commandMessageSubType`
        form (dict): A dictionary containing the form data from the request

    Returns:
        tmcvp_command_message_pb2.CommandMessage: The generated CommandMessage.

    Works almost same as :func:`commander.generate_command_message`.    

    Note for Future Upgrades:
    This function assumes that the fields message_id, correlation_id, vehicle_id, type,
    priority, provisioning_state, version, packet_status, and subtype are present
    in future proto versions of `CommandMessage` as in version TMCVP 6.3.
    If any of these headers change, the code needs to be modified.
    """
    # Create a CommandMessage and set common fields
    command_message = tmcvp_command_message_pb2.CommandMessage()

    command_message.message_id = str(uuid.uuid4())
    command_message.correlation_id = form["correlation_id"]
    command_message.vehicle_id = form["vehicle_id"]

    command_message.type = int(form["type"])

    command_message.subtype = subtype
    command_message.priority = form["priority"]
    command_message.provisioning_state = int(form["provisioning_state"])
    command_message.version = form["version"]
    command_message.time_stamp.GetCurrentTime()
    command_message.packet_status = int(form["packet_status"])

    # Select the appropriate command payload based on subtype
    command_payload = getattr(
        tmcvp_command_pb2,
        tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload",
    )()
    fill_payload(command_payload, form)

    # Set the payload in the command message
    getattr(
        command_message.command_payload,
        command_message.command_payload.DESCRIPTOR.fields[subtype].name,
    ).CopyFrom(command_payload)

    return command_message

def fill_payload(message, form):
    """
    Fills the payload message with data from the form. 

    Literally the same as :func:`utils.fill_message`
    """
    for field_descriptor in message.DESCRIPTOR.fields:
        field_name = field_descriptor.name
        field_type = field_descriptor.type
        if field_name in form and form[field_name] != "":
            # IS ENUM
            if field_type == field_descriptor.TYPE_ENUM:
                setattr(message, field_name, int(form[field_name]))
            # IS MESSAGE
            elif field_type == field_descriptor.TYPE_MESSAGE:
                # IS REPEATED MESSAGE
                if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                    num_repeated = NUM_REPEATED
                    for _ in range(num_repeated):
                        nested_payload = getattr(message, field_descriptor.name).add()
                        fill_payload(nested_payload, form)
                # IS NOT REPEATED MESSAGE
                else:
                    nested_payload = getattr(message, field_descriptor.name)
                    fill_payload(nested_payload, form)

            # IS REPEATED BASIC TYPE
            elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = NUM_REPEATED
                for _ in range(num_repeated):
                    setattr(message, field_name, form[field_name])
            # IS BASIC TYPE
            else:
                field_type = field_descriptor.type
                if field_type == field_descriptor.TYPE_DOUBLE or field_type == field_descriptor.TYPE_FLOAT:
                    setattr(message, field_name, float(form[field_name]))
                elif field_type in [field_descriptor.TYPE_INT32, field_descriptor.TYPE_INT64, field_descriptor.TYPE_UINT32, field_descriptor.TYPE_UINT64]:
                    setattr(message, field_name, int(form[field_name]))
                elif field_type == field_descriptor.TYPE_BOOL:
                    setattr(message, field_name, bool(form[field_name]))
                elif field_type == field_descriptor.TYPE_STRING:
                    setattr(message, field_name, form[field_name])
                elif field_type == field_descriptor.TYPE_BYTES:
                    setattr(message, field_name, bytes(form[field_name], 'utf-8'))
    
    return message

@socketio.on('connect')                                                         
def connect():                                                                  
    socketio.emit('message', {'hello': "Hello"})

@socketio.on('subscribe')
def handle_subscribe(data):
    print(data)
    mqtt.unsubscribe_all()
    CommandResponseTopic = "/device/" + data['vinNo'] + "/MQTTPROTOBUF/commandresponse"
    print("Subcribed to Topic: {}".format(CommandResponseTopic))
    mqtt.subscribe(CommandResponseTopic)
    # mqtt.subscribe(data['topic'])

@mqtt.on_message()
def handle_mytopic(client, userdata, message):
    print("Received Message on Topic: {}".format(message.topic))

    socketio.emit('mqtt_message', 
        {   
            'topic': message.topic,
            'message': decode_response(message.payload), 
            'messageHex': message.payload.hex(" ").upper()
        })

    return

def decode_response(rcvdMsg):
    """
    Decode and print the received MQTT message.

    Parameters:
    - rcvdMsg (bytes): The received MQTT message in bytes.

    This is equivalent to :func:`commander.decode_response`

    Important:
    This function assumes that the fields message_id, correlation_id, vehicle_id, 
    type, subtype, priority, provisioning_state, version, time_stamp, packet_status
    and return_code are present in future proto versions of `CommandResponseMessage`
    as in version TMCVP 6.3. If any of these fields change, the code needs to be
    modified. However, it is agnostic to changes `commandResponsePayload`.

    """
    try:
        # Decode and print the response based on subtype
        response_message = tmcvp_commandresponse_message_pb2.CommandResponseMessage()
        response_message.ParseFromString(rcvdMsg)

        response_payload_type = str(response_message.commandResponsePayload.WhichOneof("commandResponsePayload"))
        response_payload = getattr(response_message.commandResponsePayload, response_payload_type)

        with app.app_context():
            response_table = render_template('response_table.html', response_message=response_message, tmcvp_common_pb2=tmcvp_common_pb2, tmcvp_command_message_pb2=tmcvp_command_message_pb2, tmcvp_commandresponse_message_pb2=tmcvp_commandresponse_message_pb2, datetime=datetime)
        payload_table = utils.MessageToTable(response_payload, show_empty=True, tablefmt='unsafehtml')
        payload_table = payload_table.replace('<table>', '<table class="table table-bordered">')

        return response_table + payload_table
    except Exception as e:
        print("Error: ", e)
        return '<p class="text-danger">Parsing Failed</p>'

def TmcvpMQTTProtobufServer():
    return app


if __name__ == '__main__':
    # app.run(debug=True,use_reloader=False)
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)
