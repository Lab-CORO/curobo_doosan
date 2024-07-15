#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    rospy.loginfo("Received message: %s", str(message.payload.decode("utf-8")))

def mqtt_listener():
    rospy.init_node('mqtt_ros_node', anonymous=True)
    rospy.loginfo("Starting MQTT listener node")
    
    client = mqtt.Client("ROSListener")
    client.on_message = on_message

    client.connect("localhost", 1883,60)
    client.subscribe("Velocity")
    client.loop_forever()

if __name__ == '__main__':
    try:
        mqtt_listener()
    except rospy.ROSInterruptException:
        pass
