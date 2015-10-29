#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

topic ="testubuntucore"
payload = "None"
qos = "0"
retain = "False"

#Use this for MQTT servers needing authentication
#username = ""
#password = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to Eclipse sandbox with result code "+str(rc))
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received the message : "+str(msg.payload)+" on topic : "+str(msg.topic))


def on_publish(mosq, obj, mid):

	print("Publishing successful")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.will_set(topic, payload=None, qos=0, retain=False)
client.connect("iot.eclipse.org",1883,60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
i=1
while client.loop() == 0:
	message = "Test publish "+ str(i)	
	print("Sending on topic: "+str(topic)+" the message :"+str(message))	
	client.publish(topic, message)
	i =i +1
	time.sleep(10)# sleep for 10 seconds before next call


