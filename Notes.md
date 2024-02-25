# Notes on Flask, WTForms, Protocol Buffers and more...

These notes are a part of Flask based Web Server I build for TMCVP Protobuf Encoded Communication Testing Server.

## Protocol Buffers

### Compiling large number of .proto files.

Suppose you have a folder with ~100 .proto files. You wont do `protoc --python_out=compile_pb/ myProtoFile.proto` for each one of them.
Instead a simple shell script makes job easier.

```{code-block} bash
:lineno-start: 31

for file in *.proto; do 
    echo "Compiling $file"
    protoc --python_out=pyi_out:$1 $file
```
The `.pyi` files to help in IDEs and code editors like VsCode or PyCharm.

### Looping over all fields in protobuf messages.

The python protobuf provides an api {meth}`ListField <google.protobuf.message.Message.ListFields>`, however does not lists empty fields.
This causes fields specifically set to values like `0` to be skipped.

Another vale is to use `message.DESCRIPTOR.fields` which will list all the field descriptors for that message type. This includes empty ones. 
This creates a list of names of all fields in the message, where field is of type {class}`google.protobuf.descriptor.FieldDescriptor`
```python
[f.name for f in a.DESCRIPTOR.fields] 
```

See {meth}`protoserver.utils.MessageToTable` for entire code, but here is the gist


```{code-block} python
---
lineno-start: 250
emphasize-lines: 1,4
---

gen = message.ListFields()
## To loop over fields which are not shown in ListFields
if show_empty:
    gen = ((f, getattr(message, f.name)) for f in message.DESCRIPTOR.fields)

for field_descriptor, value in gen:
    ...
```

### Getting string name of Enum in protobuf message

Suppose we have an enum class `ExampleEnum` we can get name for corresponding int type as `ExampleEnum.Name(1)`.
In case of enum field inside a message we can use [`field.enum_type.values_by_number`](https://googleapis.dev/python/protobuf/latest/google/protobuf/descriptor.html#google.protobuf.descriptor.EnumDescriptor.values_by_number)
```{code-block} python
:lineno-start: 261

for field_descriptor, value in message.ListFields():
    field_descriptor.enum_type.values_by_number[int(sub_message)].name
```

## WTForms

I have used this for creating dynamic flask forms. See {meth}`protoserver.app.generateDynamicForm` for more deatils.

### Basic Stuff

```{code-block} python
:lineno-start: 56

class MyFLaskForm(FlaskForm):
    intField = IntegerField("Integer Field", render_kw={"class":"form-control"})
    stringField = StringField("String Field", render_kw={"placeholder": "Enter text"})
    selectField = SelectField("Select Field", choices=[(e.number, e.name) for e in enum_type.values] render_kw={"class":"form-select"})
```

### Real Stuff

```{code-block} python
:lineno-start: 201
:emphasize-lines: 7,10-11,15

def generateDynamicForm(message):
    class DynamicForm(FlaskForm):
        pass

    for field in message.DESCRIPTOR.fields:
        # {ENUM: "SelectField", INTEGER: "IntegerField", STRING: "StringField"}[field.type]
        setattr(DynamicForm, field.name, {{TYPE}}Field(field.name, **kwrgs, render_kw=...))

        if field.label == field.LABEL_REPEATED:
            nested_form = FieldList(FormField({{TYPE}}Field(field.name), **kwargs), min_entries=..., max_entries=... **kwargs)
            setattr(DynamicForm, field.name, nested_form)

        if field.type == TYPE_MESSAGE:
            # Recursion
            setattr(DynamicForm, field.name, generateDynamicForm(message[field.name]))
    
    return DynamicForm
```
This enables me to create form based on protobuf payload.

## Flask

### Best place to learn

The best place to start in my opinion is [CS50x's Web Track](https://cs50.harvard.edu/x/2020/tracks/web/finance/) <small>(This is from CS50 2020, I don't know about current versions)</small>

Another good tutorial is the [Flask's own docs](https://flask.palletsprojects.com/en/latest/tutorial/). \
<small>There may be some youtube resources, but I am not fond of video lectures. I'd rather grind my way through the docs. <a href="https://en.wikipedia.org/wiki/RTFM">RTFM</a> baby.</small>

### Ecosystem

Another wonderful thing about [Flask](inv:Flask:std:doc#index) is the eco-sysmtem around it.
- For WTForms: we have [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/)
- For MQTT: we have [Flask-MQTT](https://flask-mqtt.readthedocs.io/en/latest/)
- For SocketIO: we have [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
- And I never saw this one coming, there is literally [Flask-Rich](https://github.com/zyf722/Flask-Rich) for [Rich](https://rich.readthedocs.io/en/latest/) based text formatting and logging in Flask.
- This one's popular: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/latest/)

### Adding attributes to variables in `render_template`

So adding CSS class is as simple as: `{{ field(class="form-control") }}`

You can also add custom JavaScript function like this:
:::{code-block} html+jinja
---
lineno-start: 74
emphasize-lines: 4,5
---

<label for="{{ form.numEntries.id }}" class="form-label">{{ form.numEntries.label }}</label>
{{ 
    form.numEntries(
        onfocus="document.getElementById('numEntriesInfo').style.display='block'", 
        onblur="document.getElementById('numEntriesInfo').style.display='none'"
    ) 

}}
<label id="numEntriesInfo" class="text-muted small" style="display: none;">This field will not be included in the form.</label>
:::

### Using `render_template` outside of registered URL Route

This is just to solve an error which occured in :func:`decode_response <protoserver.app.decode_response>`.
<div style="background-color: #1A1A1A; color: white; padding: 10px;">
    <span style="color: #FF6E6E; font-weight: bold;">RuntimeError:</span>
    <span>Working outside of application context.</span>
</div>

To solve this I did:
```{code-block} python
:emphasize-lines: 4

@mqtt.on_message()
def decode_response():
    # ...
    with app.app_context():
        response_table = render_template('response_table.html', **kwargs)
    # ...
```

## SocketIO

This is what ChatGPT said when I asked about how do I pass MQTT response from background thread to front html.
> If you're receiving MQTT responses in another thread in your Flask application and you want to update the HTML template with this data, you need a mechanism to communicate between threads. Flask-SocketIO is one way to achieve real-time communication between the server and the client using WebSockets.

So this is what I needed SocketIO for

```{image} _static/socketio-dark.svg 
:align: center
:class: only-dark
```

```{image} _static/socketio-light.svg 
:align: center
:class: only-light
```