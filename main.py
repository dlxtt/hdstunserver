import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flagdic,rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("\hdstun\echo")
    client.publish("\hdstun\echo","echo",2)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_subscribe(client,suerdata,mid,qos):
    print('ok')

if __name__ == "__main__":
    mqclient = mqtt.Client()
    mqclient.on_connect = on_connect
    mqclient.on_message = on_message
    mqclient.on_subscribe = on_subscribe

    mqclient.connect("imserver.mlgb.com.cn",1883,60)


    mqclient.loop_forever()