# -*- coding: utf-8 -*-

"""
Description: This script implements an MQTT client for sending and receiving command messages for TMCVP. 
It utilizes the Paho MQTT library and Protocol Buffers for message serialization.

Author: Muhammed Abdullah Shaikh
Date Created: Feb 14, 2024
Last Modified: Feb 26, 2024
Python Version: 3.10.11
Dependencies: Paho MQTT, Protocol Buffers, protoserver
License: BSD-3-Clause License
"""

import os, sys, uuid, time
import logging
import threading
from datetime import datetime

# sys.path.append("./TataMotorsCVP630")
# Adding TataMotorsCV630 to sys path
package_dir = os.path.abspath(os.path.dirname(__file__))
tata_motors_path = os.path.join(package_dir, 'TataMotorsCVP630')
if tata_motors_path not in sys.path:
    sys.path.append(tata_motors_path)

logging.basicConfig(format='[%(asctime)s] [%(levelname)-8s] : "%(message)s"', level=logging.DEBUG, filename="commander.log", filemode="w")


import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

from protoserver import utils
from protoserver.utils import fill_message as fill_payload

import tmcvp_common_pb2
import tmcvp_command_pb2
import tmcvp_command_message_pb2
import tmcvp_commandresponse_message_pb2
# from TataMotorsCVP630 import tmcvp_common_pb2
# from TataMotorsCVP630 import tmcvp_command_pb2
# from TataMotorsCVP630 import tmcvp_command_message_pb2
# from TataMotorsCVP630 import tmcvp_commandresponse_message_pb2


MQTT_BROKER = "test.mosquitto.org"
PORT_NO = 1883

def generate_command_message(subtype):
    """
    Generate a CommandMessage with common fields and payload based on subtype from user input.

    Parameters:
        subtype (int): The subtype of the command message corresponding to `enum commandMessageSubType`

    Returns:
        tmcvp_command_message_pb2.CommandMessage: The generated CommandMessage.

    .. admonition:: For Future Changes
        :class: caution

        This function creates and sets common fields of command message such as
        ``message_id``, ``correlation_id``, ``vehicle_id``, ``type``, ``priority``, ``provisioning_state``,
        ``version``, ``time_stamp``, and ``packet_status`` to hard code values.
        If any of these fields change, the code needs to be modified. However, 
        it is agnostic to changes ``commandPayload``.

    Example::

        command_message = generate_command_message(1)
        print(command_message)
    """
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
    r"""
    Decode and print the received MQTT message.

    :param bytes rcvdMsg: The received MQTT message in bytes.

    .. admonition:: For Future Changes
        :class: caution

        This function assumes that the fields ``message_id``, ``correlation_id``, ``vehicle_id``,
        ``type``, ``subtype``, ``priority``, ``provisioning_state``, ``version``, ``time_stamp``, ``packet_status``
        and ``return_code`` are present in future proto versions of ``CommandResponseMessage``
        as in version TMCVP 6.3. If any of these fields change, the code needs to be
        modified. However, it is agnostic to changes ``commandResponsePayload``.

    Example:

    .. code-block:: python
    
            rcvd_message = b'\n$ebc4a199-67d7-4bea-9fed-d05db21e7744\x12$b82a63a2-6619-496a-8b92-be7a763db448\x1a\x11ACCDEV14012078186 \x01(\x112\x0108\x02B\x056.2.0J\t\x08\x9f\x93\xd6\xae\x06\x10\x8a\x02PLb\x05\x9a\x01\x02\x08\x01'
            decode_response(rcvd_message)
    """

    print("In Hex:\n{}".format(rcvdMsg.hex(" ").upper()))
    try:
        # Decode and print the response based on subtype
        response_message = tmcvp_commandresponse_message_pb2.CommandResponseMessage()
        response_message.ParseFromString(rcvdMsg)

        response_payload_type = str(response_message.commandResponsePayload.WhichOneof("commandResponsePayload"))
        response_payload = getattr(response_message.commandResponsePayload, response_payload_type)

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
    except Exception as e:
        print("Parsing Failed. Error: {}".format(e))

    return

def start_mqtt(client):
    """
    Configures callbacks and start the MQTT client for communication. Blocks until connection is established.
    
    Parameters:
        client (paho.mqtt.client): MQTT client object
    
    """
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
def mqtt_subscribe(vin_no='+'):
    """Subscribe to a MQTT topic for a given VIN number else uses wild card (+)

    .. hint::
        This function uses `paho.mqtt.subscribe <https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html#subscribe>`_ instead of subcribing with same client.
        Reason: I was facing issues when publishing and subcribing with the same client object. 

    Parameters:
        vin_no (str):  VIN number for MQTT topic subscription
    """
    CommandResponseTopic = "/device/" + vin_no + "/MQTTPROTOBUF/commandresponse"
    print("Subcribed to Topic: {}".format(CommandResponseTopic))
    subscribe.callback(handle_mytopic, CommandResponseTopic, hostname=MQTT_BROKER, port=PORT_NO)

VinNo = ""
CommandTopic =""
def main():

    global VinNo, CommandTopic
    # VinNo = "ACCDEV14012078186"
    VinNo = input("Enter the VIN number: ").strip()
    CommandTopic = "/device/" + VinNo + "/MQTTPROTOBUF/command"

    client = mqtt.Client(client_id="Tester_6.3")
    start_mqtt(client)

    threading.Thread(target=mqtt_subscribe, args=(VinNo,), daemon=True).start()

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
