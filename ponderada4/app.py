# python 3.6 - Envio das Mensagens

import random
import time
import cv2
import base64
import numpy as np
import pyautogui
from paho.mqtt import client as mqtt_client
from ultralytics import YOLO
import pickle


broker = 'broker.hivemq.com'
port = 1883
topic = "python/mqtt/katalan"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-katalan-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    last_frame = ""
    while True:

        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        _, jpeg_image = cv2.imencode('.jpeg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        print("q")
        pred = YOLO('../ponderada3/best.pt').predict([frame])
        msg = []
        frame_base64 = []
        for result in pred:
            if len(result.boxes) > 0:
        #frame = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
                frame_base64 = base64.b64encode(jpeg_image)
                msg = [frame_base64, result]
        if last_frame != frame_base64:
            msg_bytes = pickle.dumps(msg)
            msg_str = base64.b64encode(msg_bytes).decode('utf-8')
            result = client.publish(topic, msg_str, retain = False)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            last_frame = msg
        else:
            pass
        # result: [0, 1]

        


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()