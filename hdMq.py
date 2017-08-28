import paho.mqtt.client as mqtt
import settings
import mcQue
import stunController

TOPIC_STUN = '/hdstun/stun'
TOPIC_CLIENT = '/hdstun/client/%s'
TOPIC_SERVER = '/hdstun/server/%s'
TOPIC_MCSTATUS = '/hdstun/mcstatus/#'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flagdic,rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC_STUN)
    client.subscribe(TOPIC_MCSTATUS)
    # client.will_set("/hdstun/client", payload='okokok', qos=2, retain=True)
    # client.publish("\hdstun\echo","echo",2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic.split('/')
    print(msg.topic + " " + str(msg.payload))

    strMsg = str(msg.payload,"utf-8")

    if len(topic)<3:
        return

    #处理请求
    if topic[2]=='stun':
        print(msg.topic+" "+strMsg)
        stunController.requestProcesser(strMsg)

    #处理计算节点状态更新
    if (topic[2]=='mcstatus') and (len(topic)==4):
        pn_code = topic[3]
        mcQue.setmc(pn_code, strMsg)

def on_subscribe(client,suerdata,mid,qos):
    print('ok')

mqclient = mqtt.Client()
def mqInit():
    mqclient.on_connect = on_connect
    mqclient.on_message = on_message
    mqclient.on_subscribe = on_subscribe

    mqclient.connect(settings.MQTT_SERVER)
    mqclient.loop_forever()