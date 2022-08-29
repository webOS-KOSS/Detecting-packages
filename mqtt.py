# python 3.6

from paho.mqtt import client as mqtt_client
from multiprocessing import Process

broker = 'localhost'
port = 1883
topic = 'delivery'

class Pub():

    def __init__(self) -> None:
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = 'pub'
        self.username = 'asdf8768'
        self.password = 'asdf1234'

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client


    def publish(self, client, msg):
        self.msg = msg
        # self.client = client
        result = client.publish(self.topic, self.msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{self.msg}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic {self.topic}")


    def run(self, msg):
        client = self.connect_mqtt()
        client.loop()
        self.publish(client, msg)

class Sub():
    def __init__(self) -> None:
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = 'sub'
        self.username = 'asdf8768'
        self.password = 'asdf1234'

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        client.subscribe(topic)
        client.on_message = on_message

    def run(self):
        client = self.connect_mqtt()
        self.subscribe(client)
        client.loop_forever()
    

if __name__ == '__main__':
    pub = Pub()
    sub = Sub()
    sub_proc = Process(target=sub.run)
    pub_proc = Process(target=pub.run, args=("arrived",))
    sub_proc.start()
    pub_proc.start()