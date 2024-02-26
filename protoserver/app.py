# -*- coding: utf-8 -*-

"""
Description: Flask application for handling MQTT Protobuf messages related to TMCVP commands and telemetry.
Author: Muhammed Abdullah Shaikh
Date Created: Feb 14, 2024
Last Modified: Feb 26, 2024
Python Version: 3.10.11
Dependencies: Flask, Flask-SocketIO, Flask-MQTT, Flask-WTF, Flask-Rich, protobuf
License: BSD-3-Clause License
"""

import os
import sys
import logging
import uuid
import json
from datetime import datetime

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, FloatField, FieldList, FormField
from flask_rich import RichApplication

# sys.path.append("./TataMotorsCVP630")
# Adding TataMotorsCV630 to sys path
package_dir = os.path.abspath(os.path.dirname(__file__))
tata_motors_path = os.path.join(package_dir, 'TataMotorsCVP630')
if tata_motors_path not in sys.path:
    sys.path.append(tata_motors_path)

if not os.path.exists("logs"):
    os.mkdir("logs")

file_handler = logging.FileHandler(f'logs/server_{str(datetime.now().strftime("%Y%m%d-%H%M%S"))}.log')
file_handler.setLevel(logging.NOTSET)
file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] : %(message)s'))

logging.root.setLevel(logging.DEBUG)

from google.protobuf.json_format import MessageToJson, MessageToDict, Parse, ParseDict
import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2
import tmcvp_vehicletelemetry_message_pb2
import tmcvp_high_speed_telemetry_message_pb2
import tmcvp_ev_high_speed_telemetry_message_pb2

from protoserver import utils

MQTT_BROKER = "test.mosquitto.org"
PORT_NO = 1883

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Replace with a secret key in production
app.config['MQTT_BROKER_URL'] = MQTT_BROKER
app.config['MQTT_BROKER_PORT'] = PORT_NO
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ' '
app.config['MQTT_REFRESH_TIME'] = 5.0  # refresh time in seconds
app.config['RICH_LOGGING'] = True   # for rich logging
mqtt = Mqtt(app)
csrf = CSRFProtect(app)
socketio = SocketIO(app) 
rich = RichApplication(app)
app.logger.addHandler(file_handler)

###########################################################
##################  COMMAND RESPONSE   ####################
###########################################################

CONTROL_RENDER_KW = dict(render_kw={"class":"form-control form-control-sm"})
SELECT_RENDER_KW = dict(render_kw={"class":"form-select form-select-sm"})
class CommandMessageForm(FlaskForm):
    """
    FlaskForm for creating a Command Message.

    Attributes:
        message_id (:class:`StringField <wtforms.fields.StringField>`): Unique identifier for the message.
        correlation_id (:class:`StringField <wtforms.fields.StringField>`): Identifier for correlating messages.
        vehicle_id (:class:`StringField <wtforms.fields.StringField>`): Identifier for the associated vehicle.
        type (:class:`SelectField <wtforms.fields.SelectField>`): Type of the message (e.g., command).
        priority (:class:`StringField <wtforms.fields.StringField>`): Priority level of the message.
        provisioning_state (:class:`SelectField <wtforms.fields.SelectField>`): Provisioning state of the message.
        version (:class:`StringField <wtforms.fields.StringField>`): Version of the message.
        packet_status (:class:`SelectField <wtforms.fields.SelectField>`): Status of the packet (e.g., Live).
        subtype (:class:`SelectField <wtforms.fields.SelectField>`): Subtype of the command message.

    .. admonition:: For Future Changes
        :class: caution

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

    numEntries = IntegerField('Number of Entries for repeated type', default=1, **CONTROL_RENDER_KW)


@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    form = CommandMessageForm(request.form)

    vinNo = session.get('vin_no', '')
    if vinNo:
        _handle_subscribe({'vinNo': vinNo, 'topic': 'commandresponse'}) 
    return render_template('index.html', form=form, vin_no=vinNo, topic="commandresponse")

@app.route('/set_vin', methods=['POST'])
def set_vin():
    vin_no = request.form.get('vin_no')
    session['vin_no'] = vin_no
    app.logger.info('Setting VIN No to: %s', vin_no)
    return jsonify({'status': 'success'})


@app.route('/get_additional_fields', methods=['POST'])
def get_additional_fields():
    """
    A function to handle the ``/get_additional_fields`` route and return additional fields HTML based on the request data.

    This function is called on subtype dropdown change

    .. code:: js
        :number-lines: 131

        $('#{{ form.subtype.id }}').change( function() {
        var selectedSubtype = $(this).val();
        var numEntries = $('#{{ form.numEntries.id }}').val();

        $.ajax({
            url: '/get_additional_fields',
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf_token
                },
            data: { 'subtype': selectedSubtype, 'numEntries': numEntries },
            success: function (response) {
                $('#additionalFieldsContainer').html(response.additional_fields_html);
                }
            });
        })
    """
    subtype = request.form.get('subtype', -1)
    numEntries = int(request.form.get('numEntries', 1))
    session['numEntries'] = max(numEntries, 1)
    try:
        subtype = int(subtype)
        if subtype == -1:
            return jsonify({'additional_fields_html': ''})
    except:
        return jsonify({'additional_fields_html': ''})

    payloadType = tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload"
    command_payload = getattr(tmcvp_command_pb2, payloadType)()

    form  = generateDynamicForm(command_payload)(request.form)

    additional_fields_html = render_template('additional_fields.html', form=form)
    return jsonify({'additional_fields_html': additional_fields_html})
    
@app.route('/send_command', methods=['POST'])
def send_command():
    """
    Generate and send a command message based on the form data.

    This function extracts the subtype from the form data and generates a command message
    using the :func:`generate_command_message` function. The generated message is then serialized
    and published to the appropriate MQTT topic.

    Returns:
        (str): JSON object containing the response with status, command message as a dictionary, and the hex representation of the serialized message.
    """
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

    message_dict = utils.MessageToDict(command_message)
    app.logger.debug(f"Published CommandMessage on Topic: {CommandTopic}\n{json.dumps(message_dict, indent=4)}")
    return jsonify({
        'status': 'success',
        'message': message_dict,
        'messageHex': serialized_message.hex(' ').upper()
    })

NUM_REPEATED_MAX = 30
NUM_MIN = 1
def generateDynamicForm(payload):
    """
    Generate a dynamic form class based on the given payload.

    Works almost same as :func:`.utils.fill_message`.

    Parameters:
        payload (google.protobuf.message.Message): The message fields lled into the form.
    
    Returns:
        DynamicForm (:class:`FlaskForm <flask_wtf.FlaskForm>`): The generated form class.

    """
    class DynamicForm(FlaskForm):
        pass

    num_repeated = min(session.get('numEntries', NUM_MIN), NUM_REPEATED_MAX)
    for field_descriptor in payload.DESCRIPTOR.fields:
        field_name = field_descriptor.name
        field_type = field_descriptor.type

        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            values = field_descriptor.enum_type.values
            enum_choices = [(e.number, e.name) for e in values]
            setattr(DynamicForm, field_name, SelectField(field_name, choices=enum_choices, coerce=int, **SELECT_RENDER_KW))
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                # for _ in range(num_repeated):
                nested_payload = getattr(payload, field_descriptor.name).add()
                nested_form  = FieldList(FormField(generateDynamicForm(nested_payload), render_kw={"class":"table table-bordered"}), min_entries=num_repeated, max_entries=NUM_REPEATED_MAX, render_kw={"class":"list-group list-unstyled"})
                setattr(DynamicForm, field_name, nested_form)
            # IS NON REPEATED MESSAGE
            else:
                nested_payload = getattr(payload, field_descriptor.name)
                nested_form = generateDynamicForm(nested_payload)
                setattr(DynamicForm, field_name, nested_form)
        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            # for _ in range(num_repeated):
            #     setattr(DynamicForm, field_name, StringField(field_name, **CONTROL_RENDER_KW))
            setattr(DynamicForm, field_name, FieldList(StringField(field_name, **CONTROL_RENDER_KW), min_entries=num_repeated, max_entries=NUM_REPEATED_MAX, render_kw={"class":"list-group list-unstyled"}))
        else:
            if field_descriptor.type == field_descriptor.TYPE_DOUBLE or field_descriptor.type == field_descriptor.TYPE_FLOAT:
                setattr(DynamicForm, field_name, FloatField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type in [field_descriptor.TYPE_INT32, field_descriptor.TYPE_INT64, field_descriptor.TYPE_UINT32, field_descriptor.TYPE_UINT64]:
                setattr(DynamicForm, field_name, IntegerField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BOOL:
                setattr(DynamicForm, field_name, BooleanField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_STRING:
                setattr(DynamicForm, field_name, StringField(field_name, **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BYTES:
                setattr(DynamicForm, field_name, StringField(field_name, **CONTROL_RENDER_KW))

    return DynamicForm

def generate_command_message(subtype, form):
    """
    Generate a Command Message based on the provided subtype and form input.

    This function uses :func:`google.protobuf.json_format.ParseDict` for parsing the form data,
    as ``request.form`` is an :class:`ImmutableMultiDict <werkzeug.datastructures.ImmutableMultiDict>` object.

    Parameters:
        subtype (int): The subtype of the command message corresponding to `enum commandMessageSubType`
        form (dict): A dictionary containing the form data from the request

    Returns:
        tmcvp_command_message_pb2.CommandMessage: The generated CommandMessage.

    Works almost same as :func:`.commander.generate_command_message`.    

    """
    # Create a CommandMessage and set common fields
    command_message = tmcvp_command_message_pb2.CommandMessage()

    command_message = ParseDict(form, command_message, ignore_unknown_fields=True)

    command_message.message_id = str(uuid.uuid4())
    # command_message.correlation_id = form["correlation_id"]
    # command_message.vehicle_id = form["vehicle_id"]

    command_message.type =  tmcvp_common_pb2.eTcuMessageType.command    # Because this is Command type message

    # command_message.subtype = subtype
    # command_message.priority = form["priority"]
    # command_message.provisioning_state = int(form["provisioning_state"])
    # command_message.version = form["version"]
    command_message.time_stamp.GetCurrentTime()
    # command_message.packet_status = int(form["packet_status"])

    # Select the appropriate command payload based on subtype
    command_payload = getattr(
        tmcvp_command_pb2,
        tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload",
    )()
    payload_form = generateDynamicForm(command_payload)(form)
    # fill_payload(command_payload, form)
    command_payload = ParseDict(payload_form.data, command_payload, ignore_unknown_fields=True)

    # Cannot direct assign nested messsage so using CopyFrom
    getattr(
        command_message.command_payload,
        command_message.command_payload.DESCRIPTOR.fields[subtype].name,
    ).CopyFrom(command_payload)

    return command_message

def fill_payload(message, form):
    """
    Fills the payload message with data from the form. 

    Literally the same as :func:`.utils.fill_message`

    Warning: 
        Use :func:`google.protobuf.json_format.ParseDict` instead.

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
                    num_repeated = NUM_MIN
                    for _ in range(num_repeated):
                        nested_payload = getattr(message, field_descriptor.name).add()
                        fill_payload(nested_payload, form)
                # IS NOT REPEATED MESSAGE
                else:
                    nested_payload = getattr(message, field_descriptor.name)
                    fill_payload(nested_payload, form)

            # IS REPEATED BASIC TYPE
            elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = NUM_MIN
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

###########################################################
#####################  TELEMETRY   ########################
###########################################################

TELEMETRY_TOPICS = ['telemetry', 'highSpeedTelemetry', 'evHighSpeedTelemetry']
TELEMETRY_MESSAGES = {
    'telemetry': tmcvp_vehicletelemetry_message_pb2.VehicleTelemetryMessage,
    'highSpeedTelemetry': tmcvp_high_speed_telemetry_message_pb2.HighSpeedTelemetryMessage,
    'evHighSpeedTelemetry': tmcvp_ev_high_speed_telemetry_message_pb2.EVHighSpeedTelemetryMessage
}
@app.route('/telemetry', methods=['GET', 'POST'])
def telemetry():
    telemetryTopic = request.args.get('telemetryTopic')
    if telemetryTopic is None or telemetryTopic not in TELEMETRY_TOPICS:
        telemetryTopic = 'telemetry'
    vinNo = session.get('vin_no', '')
    if vinNo:
        _handle_subscribe({'vinNo': vinNo, 'topic': telemetryTopic}) 
    return render_template('telemetry.html', vin_no=vinNo, topic=telemetryTopic, telemetryType=telemetryTopic)

###########################################################
#######################  UTILS   ##########################
###########################################################

@socketio.on('connect')                                                         
def connect():                                                                  
    socketio.emit('message', {
        'showToast': True,
        'message': "Connected to SocketIO Client",
        'header': 'Flask Server',
        'type': 'info'
    })
    app.logger.info("Client connected")

def _handle_subscribe(data):
    mqtt.unsubscribe_all()
    MQTTTopic = "/device/" + data['vinNo'] + "/MQTTPROTOBUF/" + data['topic']
    app.logger.info("Subcribed to Topic: {}".format(MQTTTopic))
    mqtt.subscribe(MQTTTopic)
@socketio.on('subscribe')
def handle_subscribe(data):
    _handle_subscribe(data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        app.logger.info("Connected to MQTT Broker")
        socketio.emit('message', {
            'showToast': True,
            'message': "Connected to MQTT Broker",
            'header': 'MQTT',
            'type': 'success'
        })

@mqtt.on_message()
def handle_mytopic(client, userdata, message):
    """Callback function for handling MQTT messages on a specific topic.

    This function decodes the payload of the received MQTT message based on the topic
    and emits the decoded information to the connected clients through Socket.IO.

    If the decoding fails, a warning message is emitted, and the payload is marked as
    "Parsing Failed" in the Socket.IO message.

    The corresponding socket.io event is "mqtt_message" which is handled as

    .. code:: js
        :number-lines: 195

        const socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('mqtt_message', function(data) {
            showToast({
                header: 'MQTT Response received on',
                data: data.topic
            });
            $('#responseHex').html(data.messageHex);
            $('#response').html(data.message);
        });

    """
    app.logger.info("Received Message on Topic: {}".format(message.topic))
    app.logger.debug("Message payload: {}".format(message.payload.hex(" ").upper()))

    mqtt_response = None
    if message.topic.endswith("commandresponse"):
        mqtt_response = decode_response(message.payload)
    elif message.topic.lower().endswith("telemetry"):
        mqtt_response = decode_telemetry(message.topic.split('/')[-1], message.payload)

    if mqtt_response is None:
        mqtt_response = '<p class="text-danger">Parsing Failed</p>'
        socketio.emit('message', {
            'showToast': True,
            'message': "Message Parsing Failed",
            'header': 'Probuf Decoder',
            'type': 'waarning'
        })

    socketio.emit('mqtt_message', 
        {   
            'topic': message.topic,
            'message': mqtt_response, 
            'messageHex': message.payload.hex(" ").upper()
        })

    return

def decode_response(rcvdMsg):
    """
    Decode command response received in the MQTT message.

    Parameters:
        rcvdMsg (bytes): The received MQTT message in bytes.

    This is equivalent to :meth:`protoserver.commander.decode_response`

    Caution:
        This function assumes that the fields ``message_id``, ``correlation_id``, ``vehicle_id``, 
        ``type``, ``subtype``, ``priority``, ``provisioning_state``, ``version``, ``time_stamp``, 
        ``packet_status`` and ``return_code`` are present in future proto versions of
        `CommandResponseMessage` as in version TMCVP 6.3. If any of these fields change,
        the code needs to be modified. However, it is agnostic to changes ``commandResponsePayload``.

    """
    try:
        # Decode and print the response based on subtype
        response_message = tmcvp_commandresponse_message_pb2.CommandResponseMessage()
        response_message.ParseFromString(rcvdMsg)

        response_payload_type = str(response_message.commandResponsePayload.WhichOneof("commandResponsePayload"))
        response_payload = getattr(response_message.commandResponsePayload, response_payload_type)
        
        app.logger.debug("Received Command Response:\n{}".format(utils.MessageToTable(response_message)))

        with app.app_context():
            response_table = render_template('response_table.html', response_message=response_message, tmcvp_common_pb2=tmcvp_common_pb2, tmcvp_command_message_pb2=tmcvp_command_message_pb2, tmcvp_commandresponse_message_pb2=tmcvp_commandresponse_message_pb2, datetime=datetime)
        payload_table = utils.MessageToTable(response_payload, show_empty=True, tablefmt='unsafehtml')
        payload_table = payload_table.replace('<table>', '<table class="table table-bordered">')

        return response_table + payload_table
    except Exception as e:
        app.logger.error("Error in decode_response: ", exc_info=e)
        return None


def decode_telemetry(topic, rcvdMsg):
    """
    Decodes different types of telemetry messages received in MQTT Protobuf.

    Parameters:
        topic (str): The topic of the received MQTT message.
        rcvdMsg (bytes): The received MQTT message in bytes.

    Returns:
        (str): A table representation of the telemetry message.
    """
    if topic not in TELEMETRY_MESSAGES:
        app.logger.error("Unknown topic: {}".format(topic))
        return None
    try:
        telemetry_message = TELEMETRY_MESSAGES[topic]()
        telemetry_message.ParseFromString(rcvdMsg)

        response_table = utils.MessageToTable(telemetry_message, tablefmt='unsafehtml')
        response_table = response_table.replace('<table>', '<table class="table table-bordered">')

        app.logger.debug("Received Telemetry Message:\n{}".format(utils.MessageToTable(telemetry_message)))

        return response_table 
    except Exception as e:
        app.logger.error("Error in decode_response: ", exc_info=e)
        return None

@app.route('/docs')
def docs():
    external_url = url_for('static', filename='docs/html/index.html')
    return redirect(external_url)

def TmcvpMQTTProtobufServer():
    """
    This function is for wsgi server that runs the app

    .. admonition:: Examples
        :class: tip

        Using `Gunicorn`_ ::
        
            $ gunicorn -w 4 -b 0.0.0.0 'protoserver.app:TmcvpMQTTProtobufServer()'
            # or 
            $ gunicorn -w 4 -b 0.0.0.0 tmcvp-server

        Using `Waitress`_ ::

            $ waitress-serve --call protoserver.app:TmcvpMQTTProtobufServer
            # or equivalently
            $ waitress-serve --call tmcvp-server

    Returns:
        app (flask.Flask): Flask application object

    .. _Gunicorn:
        https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/

    .. _Waitress:
        https://flask.palletsprojects.com/en/3.0.x/deploying/waitress/

    """
    return app

def main():
    # app.run(debug=True,use_reloader=False)
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
