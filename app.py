import sys
import logging
from datetime import datetime

sys.path.append("V6.2proto")
logging.root.setLevel(logging.DEBUG)

from flask import Flask, render_template, request, jsonify
import uuid

from google.protobuf.json_format import MessageToJson
import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


class CommandMessageForm(FlaskForm):
    message_id = StringField('Message ID', default=str(uuid.uuid4()))
    correlation_id = StringField('Correlation ID', default='correlation-id')
    vehicle_id = StringField('Vehicle ID', default='MH12VF1121')
    type = SelectField('Type', choices=[(e.number, e.name) for e in tmcvp_common_pb2.eTcuMessageType.DESCRIPTOR.values], default=tmcvp_common_pb2.eTcuMessageType.command)
    priority = StringField('Priority', default='moderate')
    provisioning_state = SelectField('Provisioning State', choices=[(e.number, e.name) for e in tmcvp_common_pb2.eProvisioningState.DESCRIPTOR.values], default=tmcvp_common_pb2.eProvisioningState.provisioned)
    version = StringField('Version', default='V6.2')
    time_stamp = StringField('Time Stamp', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), render_kw={'readonly': True})
    packet_status = SelectField('Packet Status', choices=[(e.number, e.name) for e in tmcvp_common_pb2.PacketStatus.DESCRIPTOR.values], default=tmcvp_common_pb2.PacketStatus.Live)
    subtype = SelectField('Subtype', choices=[("", "--- Select Subtype ---")]+[(e.number, e.name) for e in tmcvp_command_message_pb2.commandMessageSubType.DESCRIPTOR.values])


@app.route('/get_subtype_fields/<int:selected_subtype>', methods=['GET'])
def get_subtype_fields(selected_subtype):
    # Replace this with logic to fetch subtype-specific fields based on the selected_subtype
    # You can use the selected_subtype value to determine the fields dynamically
    subtype_fields_html = '<label>Subtype-Specific Field:</label><input type="text" name="subtype_specific_field">'
    return jsonify({'subtype_fields_html': subtype_fields_html})

@app.route('/', methods=['GET', 'POST'])
def index():
    # form = CommandForm()
    form = CommandMessageForm()

    print(form.data)

    return render_template('index.html', form=form)


def generate_payload_fields(payload):
    payload_html = ""
    for field_descriptor in payload.DESCRIPTOR.fields:
        field_name = field_descriptor.name
        field_type = field_descriptor.type

        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            values = field_descriptor.enum_type.values
            enum_choices = [(e.number, e.name) for e in values]
            payload_html += f'<label>{field_name}:</label><select name="{field_name}">'
            payload_html += '<option value="">-- Select --</option>'
            for choice in enum_choices:
                payload_html += f'<option value="{choice[0]}">{choice[1]}</option>'
            payload_html += '</select><br>'
        
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = 2
                for _ in range(num_repeated):
                    payload_html += f'<label>{field_name}:</label><br>'
                    nested_payload = getattr(payload, field_descriptor.name).add()
                    payload_html += f"<div>{generate_payload_fields(nested_payload)}</div><br>"
            # IS NON REPEATED MESSAGE
            else:
                payload_html += f'<label>{field_name}:</label><br>'
                nested_payload = getattr(payload, field_descriptor.name)
                payload_html += f"<div>{generate_payload_fields(nested_payload)}</div><br>"

        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            num_repeated = 2
            for _ in range(num_repeated):
                payload_html += f'<label>{field_name}:</label><input type="text" name="{field_name}"><br>'
        else:
            payload_html += f'<label>{field_name}:</label><input type="text" name="{field_name}"><br>'
        
    return payload_html

# Your Flask app route for handling dynamic fields
@app.route('/get_dynamic_fields', methods=['POST'])
def get_dynamic_fields():
    subtype = request.form.get('subtype')
    if not subtype:
        return ""
    
    subtype = int(subtype)
    payloadType = tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload"
    command_payload = getattr(tmcvp_command_pb2, payloadType)()

    dynamic_fields_html = f"<h3>{payloadType}</h3>"

    dynamic_fields_html += generate_payload_fields(command_payload)

    return dynamic_fields_html


if __name__ == '__main__':
    app.run(debug=True)
