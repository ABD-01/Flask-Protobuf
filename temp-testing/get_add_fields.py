import sys

from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, FloatField, FieldList, FormField

import tmcvp_command_pb2
import tmcvp_command_message_pb2

from app import app


CONTROL_RENDER_KW = dict(render_kw={"class":"form-control form-control-sm"})
SELECT_RENDER_KW = dict(render_kw={"class":"form-select form-select-sm"})
NUM_REPEATED_MAX = 30
NUM_MIN = 1
def generateDynamicForm(payload, prefix=""):

    class DynamicForm(FlaskForm):
        pass

    
    # num_repeated = min(session.get('numEntries', NUM_MIN), NUM_REPEATED_MAX)
    num_repeated = 2
    for i, field_descriptor in enumerate(payload.DESCRIPTOR.fields):
        field_name = field_descriptor.name
        field_type = field_descriptor.type

        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            values = field_descriptor.enum_type.values
            enum_choices = [(e.number, f"Enum-Options-{e.number}") for e in values]
            setattr(DynamicForm, f"{prefix}Field-{i}", SelectField(f"{prefix}Field-{i}", choices=enum_choices, coerce=int, **SELECT_RENDER_KW))
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                print(f"{field_name} i.e. {prefix}Field-{i} has repeated message")
                # for _ in range(num_repeated):
                nested_payload = getattr(payload, field_descriptor.name).add()
                nested_form  = FieldList(FormField(generateDynamicForm(nested_payload, "Nested-"+prefix), render_kw={"class":"table table-bordered"}), min_entries=num_repeated, max_entries=NUM_REPEATED_MAX, render_kw={"class":"list-group list-unstyled"})
                setattr(DynamicForm, f"{prefix}Field-{i}", nested_form)
            # IS NON REPEATED MESSAGE
            else:
                nested_payload = getattr(payload, field_descriptor.name)
                nested_form = generateDynamicForm(nested_payload, "Nested-"+prefix)
                setattr(DynamicForm, f"{prefix}Field-{i}", nested_form)
        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            print(f"{field_name}  i.e. {prefix}Field-{i}  has repeated basic type")
            # for _ in range(num_repeated):
            #     setattr(DynamicForm, field_name, StringField(field_name, **CONTROL_RENDER_KW))
            setattr(DynamicForm, f"{prefix}Field-{i}", FieldList(StringField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW), min_entries=num_repeated, max_entries=NUM_REPEATED_MAX, render_kw={"class":"list-group list-unstyled"}))
        else:
            if field_descriptor.type == field_descriptor.TYPE_DOUBLE or field_descriptor.type == field_descriptor.TYPE_FLOAT:
                setattr(DynamicForm, f"{prefix}Field-{i}", FloatField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW))
            elif field_descriptor.type in [field_descriptor.TYPE_INT32, field_descriptor.TYPE_INT64, field_descriptor.TYPE_UINT32, field_descriptor.TYPE_UINT64]:
                setattr(DynamicForm, f"{prefix}Field-{i}", IntegerField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BOOL:
                setattr(DynamicForm, f"{prefix}Field-{i}", BooleanField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_STRING:
                setattr(DynamicForm, f"{prefix}Field-{i}", StringField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW))
            elif field_descriptor.type == field_descriptor.TYPE_BYTES:
                setattr(DynamicForm, f"{prefix}Field-{i}", StringField(f"{prefix}Field-{i}", **CONTROL_RENDER_KW))

    return DynamicForm


@app.route('/getadd')
def get_add_field():
    with open("add_fields.js",'w') as file:
        file.write("function get_additional_fields(subtype, numEntries){")
        for e in tmcvp_command_message_pb2.commandMessageSubType.DESCRIPTOR.values:
                payloadType = e.name + "Payload"
                command_payload = getattr(tmcvp_command_pb2, payloadType)()
                # print("Rendering template for " + str(e.number) + " : " + e.name)
                form  = generateDynamicForm(command_payload)()
                additional_fields_html = render_template('additional_fields.html', form=form).strip()
                file.write(f'''
    {"// Handle repetition Here" if e.number in [4, 12, 27, 31] else ""}
    if (subtype == {e.number}) {{
        return `{additional_fields_html}`;
    }}'''
                    )
                file.write("\n")
        file.write("}")
    return 'Done'

def main():
    app.run(debug=True,use_reloader=False)
    # socketio.run(app, debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()