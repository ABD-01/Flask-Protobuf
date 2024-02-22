# This file contains utility functions to handle Protocol Buffer messages
# It provides functionalities to fill protobuf messages based on user input,
# convert protobuf messages to dictionary and display the message content in a tabular format
# Author: Muhammed Abdullah Shaikh
# Date: 14 Feb 2024
# Version: 1.0

from tabulate import tabulate

TYPE_TO_STRING = {
    1: "DOUBLE",
    2: "FLOAT",
    3: "INT64",
    4: "UINT64",
    5: "INT32",
    6: "FIXED64",
    7: "FIXED32",
    8: "BOOL",
    9: "STRING",
    10: "GROUP",
    11: "MESSAGE",
    12: "BYTES",
    13: "UINT32",
    14: "ENUM",
    15: "SFIXED32",
    16: "SFIXED64",
    17: "SINT32",
    18: "SINT64",
}

def get_int(prompt):
    """A function that takes a prompt as input and repeatedly prompts the user for input until a valid integer is entered. 

    Parameters:
        prompt (str): The prompt to display to the user.
    
    Returns:
        int: The user's input as an integer.

    """
    while True:
        try:
            return int(input(prompt), 10)
        except ValueError:
            pass

def get_user_input_by_type(field_descriptor):
    """
    Gets user input based on provided field descriptor type.

    Parameters:
        field_descriptor (google.protobuf.descriptor.FieldDescriptor): The field descriptor of the field to get user input for.

    Returns:
        Any: The user input based on the field descriptor type.

    """
    TYPE_DOUBLE         = 1
    TYPE_FLOAT          = 2
    TYPE_INT64          = 3
    TYPE_UINT64         = 4
    TYPE_INT32          = 5
    TYPE_FIXED64        = 6
    TYPE_FIXED32        = 7
    TYPE_BOOL           = 8
    TYPE_STRING         = 9
    TYPE_GROUP          = 10
    TYPE_MESSAGE        = 11
    TYPE_BYTES          = 12
    TYPE_UINT32         = 13
    TYPE_ENUM           = 14
    TYPE_SFIXED32       = 15
    TYPE_SFIXED64       = 16
    TYPE_SINT32         = 17
    TYPE_SINT64         = 18
    MAX_TYPE            = 18
    field_type = field_descriptor.type

    while True:
        user_input = input(f"Enter a value (type: {TYPE_TO_STRING[field_type]}) for {field_descriptor.name} (or press Enter to skip):\n").strip()

        # Skip if user input is empty
        if not user_input:
            return None

        try:
            if field_type == TYPE_DOUBLE or field_type == TYPE_FLOAT:
                return float(user_input)
            elif field_type in [TYPE_INT64, TYPE_UINT64, TYPE_INT32, TYPE_FIXED64, TYPE_FIXED32, TYPE_UINT32, TYPE_SFIXED32, TYPE_SFIXED64, TYPE_SINT32, TYPE_SINT64]:
                return int(user_input)
            elif field_type == TYPE_BOOL:
                if user_input.lower() == 'true' or user_input.lower() == 't' or user_input.lower() == '1':
                    return True
                elif user_input.lower() == 'false' or user_input.lower() == 'f' or user_input.lower() == '0':
                    return False
                else:
                    print("Invalid input. Please enter 1/[t]rue or 0/[f]alse.")
                    raise ValueError("Invalid input.")
            elif field_type == TYPE_STRING:
                return str(user_input)
            elif field_type == TYPE_BYTES:
                return bytes(user_input, 'utf-8')
            else:
                raise ValueError("Invalid field type")
        except ValueError:
            print("Invalid input. Please enter a valid value.")

# Function to get user input for an enum field
def get_enum_input(enum_type):
    """
    Get user input for selecting an enum value.

    Parameters:
    - enum_type (google.protobuf.descriptor.EnumDescriptor): The enum type descriptor.

    Returns:
    - Enum value corresponding to the user's choice.

    This function prints the available options for the given enum type,
    prompts the user to enter the number corresponding to their choice,
    and returns the selected enum value. The user can press Enter to skip
    making a selection. If the entered input is invalid, the function will
    print an error message and prompt the user again.

    Example:
    ```
    from example_pb2 import ExampleEnum
    selected_value = get_enum_input(ExampleEnum.DESCRIPTOR)
    ```

    """
    values = enum_type.values
    print(f"Select from {len(values)} options for {enum_type.name}:")
    max_len = max(len(value.name) for value in values) # find the longest key
    for enum_value in values:
        print(f"{enum_value.name.ljust(max_len + 5, '.')}{enum_value.number}")
    while True:
        try:
            selected_enum = input("Enter the number corresponding to your choice (or press Enter to skip): ").strip()
            if not selected_enum:
                return None
            selected_enum = int(selected_enum)
            return enum_type.values[selected_enum].number
        except (ValueError, KeyError, IndexError):
            print("Invalid input. Please enter a valid number.")

# Function to fill a message based on user input
def fill_message(message):
    """
    Fill the given protocol buffer message with user input for each field.
    """
    for field_descriptor in message.DESCRIPTOR.fields:
        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            user_input = get_enum_input(field_descriptor.enum_type)
            if user_input is not None:
                setattr(message, field_descriptor.name, user_input)
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = get_int(f"Enter the number of {field_descriptor.name} elements (or enter 0 to skip): ")
                for _ in range(num_repeated):
                    nested_message = getattr(message, field_descriptor.name).add()
                    fill_message(nested_message)
            # IS NON REPEATED MESSAGE
            else:
                user_input = input(f"Do you want to fill {field_descriptor.name} ? (yes/no): ")
                if user_input.lower() in ['yes', 'y']:
                    nested_message = getattr(message, field_descriptor.name)
                    fill_message(nested_message)

        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            num_repeated = get_int(f"Enter the number of {field_descriptor.name} elements (or enter 0 to skip): ")
            for _ in range(num_repeated):
                user_input = get_user_input_by_type(field_descriptor)
                if user_input is not None:
                    getattr(message, field_descriptor.name).append(user_input)

        else:
            user_input = get_user_input_by_type(field_descriptor)
            if user_input is not None:
                setattr(message, field_descriptor.name, user_input)
        
    return message

def MessageToDict(message):
    """
    Convert a protocol buffer message into a dictionary representation.

    Directly stolen from `Stackoverflow <https://stackoverflow.com/a/57359749>`_
    I am not using `google.protobuf.json_format.MessageToDict<https://googleapis.dev/python/protobuf/latest/google/protobuf/json_format.html#google.protobuf.json_format.MessageToDict>`_
    because the keynames are not being matched properly.

    Args:
        message(google.protobuf.message.Message): The protocol buffer message to be converted.

    Returns:
        dict: A dictionary representation of the protocol buffer message.
    """
    message_dict = {}
    
    for descriptor, value in message.ListFields():
        key = descriptor.name
        # value = getattr(message, descriptor.name)
        
        if descriptor.label == descriptor.LABEL_REPEATED:
            message_list = []
            
            for sub_message in value:
                if descriptor.type == descriptor.TYPE_MESSAGE:
                    message_list.append(MessageToDict(sub_message))
                else:
                    message_list.append(sub_message)
            
            message_dict[key] = message_list
        else:
            if descriptor.type == descriptor.TYPE_MESSAGE:
                message_dict[key] = MessageToDict(value)
            else:
                message_dict[key] = value
    
    return message_dict

def MessageToTable(message, show_empty=False, tablefmt="grid"):
    """
    Generates a table representation of the given message.

    Parameters:
        message (google.protobuf.message.Message): The message to convert to a table.
        show_empty (bool): Whether to show empty fields. Defaults to False.
        tablefmt (str): The format of the table. Defaults to "grid".

    .. tip::
        The method `ListFields <https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.ListFields>`_ 
        only returns non-empty values which may cause fields set to `0` to be skipped.
        For instance the field `return_code` was being skipped in case of successful return.
        Using `show_empty=True` will show empty fields in the table but I recommend to avoid it as it will make the table too large with unnecessary empty fields.

    Returns:
        A table representation of the message.
    """
    headers = ['Field Index', "Name", "Type", "Content"]
    table = []
    gen = message.ListFields()
    if show_empty:
        gen = ((f, getattr(message, f.name)) for f in message.DESCRIPTOR.fields)

    for field_descriptor, value in gen:
        field_type = TYPE_TO_STRING[field_descriptor.type]
        if field_descriptor.label == field_descriptor.LABEL_REPEATED:
            for sub_message in value:
                if field_descriptor.type == field_descriptor.TYPE_MESSAGE:
                    table.append([field_descriptor.number, field_descriptor.name, field_type, MessageToTable(sub_message, show_empty=show_empty, tablefmt=tablefmt)])
                else:
                    table.append([field_descriptor.number, field_descriptor.name, field_type, sub_message])
            
        else:
            if field_descriptor.type == field_descriptor.TYPE_MESSAGE:
                table.append([field_descriptor.number, field_descriptor.name, field_type, MessageToTable(value, show_empty=show_empty, tablefmt=tablefmt)])
            else:
                table.append([field_descriptor.number, field_descriptor.name, field_type, value])
    return tabulate(table, headers=headers, tablefmt=tablefmt)
