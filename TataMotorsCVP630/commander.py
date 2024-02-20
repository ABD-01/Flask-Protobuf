import sys, uuid, time
import logging
import threading
from datetime import datetime

# sys.path.append("V6_3proto")
logging.basicConfig(format='[%(asctime)s] [%(levelname)-8s] : "%(message)s"', level=logging.DEBUG, filename="commander.log", filemode="w")


import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

import utils
from utils import fill_message as fill_payload

import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2


MQTT_BROKER = "test.mosquitto.org"
PORT_NO = 1883

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

    response_payload_type = str(response_message.commandResponsePayload.WhichOneof("commandResponsePayload"))
    response_payload = getattr(response_message.commandResponsePayload, response_payload_type)

    print("In Hex:\n{}".format(rcvdMsg.hex(" ").upper()))
    print("message_id:", response_message.message_id)
    print("correlation_id:", response_message.correlation_id)
    print("vehicle_id:", response_message.vehicle_id)
    print("type:", tmcvp_common_pb2.eTcuMessageType.Name(response_message.type))
    print("subtype:", tmcvp_command_message_pb2.commandMessageSubType.Name(response_message.subtype))
    print("priority:", response_message.priority)
    print("provisioning_state:", tmcvp_common_pb2.eProvisioningState.Name(response_message.provisioning_state))
    print("version:", response_message.version)
    print("time_stamp:", datetime.fromtimestamp(response_message.time_stamp.seconds).strftime('%Y-%m-%d %H:%M:%S'))
    print("packet_status:", tmcvp_common_pb2.PacketStatus.Name(response_message.packet_status))
    print("return_code:", tmcvp_commandresponse_message_pb2.eReturnCode.Name(response_message.return_code))
    print("commandResponsePayload:\n{}".format(utils.MessageToTable(response_payload, show_empty=True)))

    logging.info("Command Response:\n{}".format(utils.MessageToTable(response_message)))

    return

def start_mqtt(client):

    def on_connect(client, userdata, flags, rc):
        print("Client with id: " + str(client._client_id) + " Connected")
        logging.info("Connected with result code %s", str(rc))
        # client.subscribe("/device/+/MQTTPROTOBUF/commandresponse")

    def on_message(client, userdata, msg):
        msg_len = len(msg.payload)
        logging.info("Topic: %s Received Message: %s)", msg.topic, msg.payload)
    
    def on_publish(client, userdata, mid):
        logging.info("Message Published: %s", str(mid))

    # @client.topic_callback("/device/+/MQTTPROTOBUF/commandresponse")
    # def handle_mytopic(client, userdata, message):
    #     # logging.info("Received Message on Topic: %s\n", message.topic)
    #     print("Received Message on Topic: {}".format(message.topic))
    #     decode_response(message.payload)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish


    client.connect(MQTT_BROKER, PORT_NO)

    client.loop_start()

    # Wait for connection
    print("Waiting for connection...")
    while not client.is_connected():
        time.sleep(0.1)

    # client.subscribe("/device/ABC/MQTTPROTOBUF/commandresponse")

def handle_mytopic(client, userdata, message):
    # logging.info("Received Message on Topic: %s\n", message.topic)
    print("Received Message on Topic: {}".format(message.topic))
    decode_response(message.payload)
def mqtt_subscribe():
    subscribe.callback(handle_mytopic, "/device/+/MQTTPROTOBUF/commandresponse", hostname=MQTT_BROKER, port=PORT_NO)

VinNo = ""
CommandTopic =""
def main():

    global VinNo, CommandTopic
    # VinNo = "ACCDEV14012078186"
    VinNo = input("Enter the VIN number: ")
    CommandTopic = "/device/" + VinNo + "/MQTTPROTOBUF/command"

    client = mqtt.Client(client_id="Tester_6.2")
    start_mqtt(client)

    threading.Thread(target=mqtt_subscribe, daemon=True).start()

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
            logging.info("Published CommandMessage:\n%s", utils.MessageToTable(command_message))

            input("Press Enter to continue...")

        except KeyboardInterrupt:
            break
        finally:
            client.loop_stop()


if __name__ == "__main__":
    main()
