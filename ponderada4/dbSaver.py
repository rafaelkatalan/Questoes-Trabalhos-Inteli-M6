# python3.6 - Receber

import random
import cv2
import base64
import numpy as np
from paho.mqtt import client as mqtt_client
import pickle
import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    result = Column(String)

engine = create_engine('sqlite:///predictions.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

broker = 'broker.hivemq.com'
port = 1883
topic = "python/mqtt/katalan"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
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

def subscribe(client: mqtt_client):



    def on_message(client, userdata, msg):
    # decode and deserialize the message
        msg_bytes = base64.b64decode(msg.payload)
        msg = pickle.loads(msg_bytes)
    # process the message
        file_name = f'./images/image-{time.time()}.jpeg'
        if len(msg)!=2:
            print("bad message")
            return
        frame_base64, result = msg
        #file_path = os.path.join('images', file_name)
        frame = cv2.imdecode(np.frombuffer(base64.b64decode(frame_base64), np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite(file_name, frame)

    # save image reference and result to database
        
        result_str = str(result)  # convert result to string
        prediction = Prediction(image=file_name, result=result_str)
        session = Session()
        session.add(prediction)
        session.commit()
        print("saved")



    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()