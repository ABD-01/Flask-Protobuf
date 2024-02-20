import paho.mqtt.client as mqtt
import logging

logging.root.setLevel(logging.DEBUG)


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code %s", str(rc))
    client.subscribe("Accolade_Testing")
    client.subscribe("/device/+/MQTTPROTOBUF/command")


# def on_message(client, userdata, msg):
#     msg_len = len(msg.payload)
#     logging.info("Topic: %s Received Message: %s)", msg.topic, msg.payload)


mqttBroker = "test.mosquitto.org"
client = mqtt.Client("TestClient")

client.on_connect = on_connect
# client.on_message = on_message

client.connect(mqttBroker, 1883)

client.loop_start()

@client.topic_callback("/device/+/MQTTPROTOBUF/command")
def handle_mytopic(client, userdata, message):
    logging.debug("Callback from handle_mytopic")
    logging.info("Topic: %s \nReceived Message: %s)", message.topic, message.payload)


while True:
    user_input = input()
    client.publish("/device/ABC/MQTTPROTOBUF/commandresponse", user_input)