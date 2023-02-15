# Publish to ping
# Subscribe to pong

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("jpogue/pong")
    client.message_callback_add("jpogue/pong", on_message_from_pong)

#Custom message callback for IP info.
def on_message_from_pong(client, userdata, message):
   time.sleep(1)
   print("Custom callback  - Pong: "+message.payload.decode())
   client.publish("jpogue/ping", f"{int(message.payload.decode()) + 1}")

if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    #attach the on_message_from_pong() callback function defined above to the mqtt client
    client.on_message = on_message_from_pong
    client.connect(host="172.20.10.6", port=1883, keepalive=60)

    # start the ping-pong chain by publishing the first number to ping
    userNumber = input("Pick a number: ")
    client.publish("jpogue/ping", f"{userNumber}")
    print("Starting ping-pong!!")
    time.sleep(1)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_forever()