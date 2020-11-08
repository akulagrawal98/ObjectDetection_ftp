import paho.mqtt.client as mqtt

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.on_publish = on_publish

f=open("img.jpeg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("project",byteArr,0)

client.loop_forever()
