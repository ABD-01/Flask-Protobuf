from tabulate import tabulate
import example_pb2
from google.protobuf.json_format import MessageToJson

TYPE_TO_STRING = {
    1: "TYPE_DOUBLE",
    2: "TYPE_FLOAT",
    3: "TYPE_INT64",
    4: "TYPE_UINT64",
    5: "TYPE_INT32",
    6: "TYPE_FIXED64",
    7: "TYPE_FIXED32",
    8: "TYPE_BOOL",
    9: "TYPE_STRING",
    10: "TYPE_GROUP",
    11: "TYPE_MESSAGE",
    12: "TYPE_BYTES",
    13: "TYPE_UINT32",
    14: "TYPE_ENUM",
    15: "TYPE_SFIXED32",
    16: "TYPE_SFIXED64",
    17: "TYPE_SINT32",
    18: "TYPE_SINT64",
}

def get_user_input_by_type(field_descriptor):
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
        user_input = input(f"Enter a value for {field_descriptor.name} (or press Enter to skip): ").strip()

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

# Function to fill a payload based on user input
def fill_payload(payload):
    for field_descriptor in payload.DESCRIPTOR.fields:
        # IS ENUM
        if  field_descriptor.type == field_descriptor.TYPE_ENUM:
            user_input = get_enum_input(field_descriptor.enum_type)
            if user_input is not None:
                setattr(payload, field_descriptor.name, user_input)
        # IS MESSAGE
        elif field_descriptor.type == field_descriptor.TYPE_MESSAGE:
            # IS REPEATED MESSAGE
            if field_descriptor.label == field_descriptor.LABEL_REPEATED:
                num_repeated = int(input(f"Enter the number of {field_descriptor.name} elements (or enter 0 to skip): "))
                for _ in range(num_repeated):
                    nested_payload = getattr(payload, field_descriptor.name).add()
                    fill_payload(nested_payload)
            # IS NON REPEATED MESSAGE
            else:
                user_input = input(f"Do you want to fill {field_descriptor.name} ? (yes/no): ")
                if user_input.lower() in ['yes', 'y']:
                    nested_payload = getattr(payload, field_descriptor.name)
                    fill_payload(nested_payload)

        # IS REPEATED BASIC TYPE
        elif field_descriptor.label == field_descriptor.LABEL_REPEATED:
            num_repeated = int(input(f"Enter the number of {field_descriptor.name} elements (or enter 0 to skip): "))
            for _ in range(num_repeated):
                user_input = get_user_input_by_type(field_descriptor)
                if user_input is not None:
                    getattr(payload, field_descriptor.name).append(user_input)

        else:
            user_input = get_user_input_by_type(field_descriptor)
            if user_input is not None:
                setattr(payload, field_descriptor.name, user_input)
        
    return payload

def MessageToDict(message):
    # ref: https://stackoverflow.com/a/57359749
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

def MessageToTable(message):
    headers = ['Field Index', "Name", "Type", "Content"]
    table = []
    for field_descriptor in message.DESCRIPTOR.fields:
        value = getattr(message, field_descriptor.name)
        field_type = TYPE_TO_STRING[field_descriptor.type]
        if field_descriptor.label == field_descriptor.LABEL_REPEATED:
            for sub_message in value:
                if field_descriptor.type == field_descriptor.TYPE_MESSAGE:
                    table.append([field_descriptor.number, field_descriptor.name, field_type, MessageToTable(sub_message)])
                else:
                    table.append([field_descriptor.number, field_descriptor.name, field_type, sub_message])
            
        else:
            if field_descriptor.type == field_descriptor.TYPE_MESSAGE:
                table.append([field_descriptor.number, field_descriptor.name, field_type, MessageToTable(value)])
            else:
                table.append([field_descriptor.number, field_descriptor.name, field_type, value])
    return tabulate(table, headers=headers, tablefmt="grid")



def main():
    message = example_pb2.ExampleMessage()
    fill_payload(message)
    # print(message)
    # json_proto = MessageToJson(message)
    # print(json_proto)
    # dict_proto = MessageToDict(message)
    # print(dict_proto)
    print(" ".join("{:02X}".format(s) for s in message.SerializeToString()))

    table_proto = MessageToTable(message)
    print(table_proto)

if __name__ == "__main__":
    main()