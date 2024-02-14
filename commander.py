import sys, uuid
import logging

sys.path.append("V6.2proto")
logging.root.setLevel(logging.DEBUG)

import paho.mqtt.client as mqtt

import utils
from utils import fill_message as fill_payload

import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2


def generate_command_message(subtype):
    # Create a CommandMessage and set common fields
    command_message = tmcvp_command_message_pb2.CommandMessage()

    command_message.message_id = str(uuid.uuid4())
    command_message.correlation_id = "correlation-id"
    command_message.vehicle_id = "MH12VF1121"

    command_message.type = tmcvp_common_pb2.eTcuMessageType.command

    command_message.subtype = subtype
    command_message.priority = "moderate"
    command_message.provisioning_state = tmcvp_common_pb2.eProvisioningState.provisioned
    command_message.version = "V6.2"
    command_message.time_stamp.GetCurrentTime()
    command_message.packet_status = tmcvp_common_pb2.PacketStatus.Live

    # Select the appropriate command payload based on subtype
    command_payload = getattr(
        tmcvp_command_pb2,
        tmcvp_command_message_pb2.commandMessageSubType.Name(subtype) + "Payload",
    )()
    fill_payload(command_payload)

    # Set the payload in the command message
    getattr(
        command_message.command_payload,
        command_message.command_payload.DESCRIPTOR.fields[subtype].name,
    ).CopyFrom(command_payload)

    return command_message

def decode_response(rcvdMsg):
    # Decode and print the response based on subtype
    response_message = tmcvp_commandresponse_message_pb2.CommandResponseMessage()
    response_message.ParseFromString(rcvdMsg)

    print("In Hex:\n", rcvdMsg.hex(" ").upper())
    print("In Table Format:\n{}".format(utils.MessageToTable(response_message)))


def start_mqtt(client):

    def on_connect(client, userdata, flags, rc):
        logging.info("Connected with result code %s", str(rc))
        client.subscribe("Accolade_Testing")
        client.subscribe("/device/+/MQTTPROTOBUF/commandresponse")

    def on_message(client, userdata, msg):
        msg_len = len(msg.payload)
        logging.info("Topic: %s Received Message: %s)", msg.topic, msg.payload)
    
    def on_publish(client, userdata, mid):
        logging.info("Message Published: %s", str(mid))

    @client.topic_callback("/device/+/MQTTPROTOBUF/commandresponse")
    def handle_mytopic(client, userdata, message):
        logging.debug("Callback from handle_mytopic")
        logging.info("Received Message on Topic: %s\n", message.topic)
        decode_response(message.payload)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    mqttBroker = "test.mosquitto.org"
    portNo = 1883
    client.connect(mqttBroker, portNo)

    client.loop_start()


def main():

    VinNo = "ACCDEV14012078186"
    CommandTopic = "/device/" + VinNo + "/MQTTPROTOBUF/command"

    client = mqtt.Client(client_id="Tester_6.2")
    start_mqtt(client)

    while True:
        try:
            subtype = utils.get_enum_input(tmcvp_command_message_pb2.commandMessageSubType.DESCRIPTOR)
            while subtype is None:
                print("Invalid subtype.")
                subtype = utils.get_enum_input(tmcvp_command_message_pb2.commandMessageSubType.DESCRIPTOR)

            # Generate and print the command message
            command_message = generate_command_message(subtype)
            print("Generated CommandMessage:")
            print("Serialized Format (in Hex):")
            serialized_message = command_message.SerializeToString()
            print(serialized_message.hex(" ").upper())
            # print("Table format:\n", utils.MessageToTable(command_message))

            client.publish(CommandTopic, serialized_message)

            input()

        except KeyboardInterrupt:
            break
        finally:
            client.loop_stop()


if __name__ == "__main__":
    main()
