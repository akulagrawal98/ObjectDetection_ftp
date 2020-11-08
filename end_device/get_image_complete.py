import paho.mqtt.client as mqtt #import the client1
import time
import os
import cv2
#import file
############
def on_message(client, userdata, message):
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)
	msg=str(message.payload.decode("utf-8"))
	if(msg=="image_ready"):
		os.system('python3 get_from_ftp.py')
		var=cv2.imread('image_class.jpeg')
		cv2.imshow('Detected',var)
		cv2.waitKey(0)
		cv2.destroyAllWindows()	



########################################
broker_address="192.168.1.14"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","ready")
client.subscribe("ready")
#print("Publishing message to topic","project")
#client.publish("project","OFF")
time.sleep(1000) # wait

#client.loop_stop() #stop the loop
