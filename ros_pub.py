#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray

def publish_to_ros_topic():
    rospy.init_node('ros_publisher_node', anonymous=True)
    pub = rospy.Publisher('/dsr_joint_velocity_controller/command', Float64MultiArray, queue_size=10)
    rospy.loginfo("ROS Publisher node initialized")

    # Message à publier sur le topic ROS
    message = Float64MultiArray()
    message.data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        pub.publish(message)
        rospy.loginfo(f"Published message to /dsr_joint_velocity_controller/command: {message.data}")
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_to_ros_topic()
    except rospy.ROSInterruptException:
        pass
