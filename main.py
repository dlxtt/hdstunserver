import hdMq

if __name__ == "__main__":
    hdMq.mqInit()
    # mqclient = mqtt.Client()
    # mqclient.on_connect = on_connect
    # mqclient.on_message = on_message
    # mqclient.on_subscribe = on_subscribe
    #
    # mqclient.connect("imserver.mlgb.com.cn",1883,60)
    #
    #
    # mqclient.loop_forever()