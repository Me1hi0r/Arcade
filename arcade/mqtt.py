import paho.mqtt.client as mqtt
from time import sleep

# from .models import Player


MQTT_HOST = "192.168.10.1"
MQTT_PORT = 1883

def on_connect(client, user_data, flags, rc):
    ignore = user_data
    ignore = flags
    
    print("MQTT: Connected, rc: " + str(rc))
    client.subscribe("/er/card")
    client.subscribe("/er/finish")
    client.subscribe("/er/player")
    print('subscribe')


def on_message(client, userdata, message):
    print("Received message [" + str(message.payload) + "] on topic ["
    + message.topic + "]")
    
    if message.topic == '/er/finish':
        msg = message.payload

        quest_name, id_card, score = msg.decode("utf-8").split('|')
        print(quest_name, id_card, score)
        print('--------')

        print('--------')
        p = Player.objects.all()
        print(len(p))



def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

def mqtt_routine():
    print("routin mqtt")
    client.connect(MQTT_HOST, MQTT_PORT, 6)
    print(f'MQTT: Connecting {MQTT_HOST}:{MQTT_PORT} ...')

    # while True: client.loop_start() # sleep(0.05)
