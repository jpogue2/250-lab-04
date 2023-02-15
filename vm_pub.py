"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    
    #get IP address
    ip_address=socket.gethostbyname("localhost")

    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    # Connect to the broker
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    # Continue publishing ip address, date, and time to the broker
    while True:
        
        #replace user with your USC username in all subscriptions
        client.publish("jpogue/ipinfo", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)

        #get date and time 
        dtObject = datetime.now()

        #publish date and time in their own topics
        print("Publishing date")
        client.publish("jpogue/date", f"{dtObject.date()}")

        time.sleep(4)

        print("Publishing time")
        client.publish("jpogue/time", f"{dtObject.time()}")

        time.sleep(4)

        #publish something random on the default topic
        print("Publishing something random")
        client.publish("jpogue/random", f"The quick brown fox jumps over the lazy dog.")

        time.sleep(4)