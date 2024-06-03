#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray

def joint_velocity_publisher():
    rospy.init_node('joint_velocity_publisher', anonymous=True)
    pub = rospy.Publisher('/dsr_joint_velocity_controller/command', Float64MultiArray, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        velocities = Float64MultiArray()
        velocities.data = [1.0, 0.5, -0.5, 1.5, -1.0, 0.0]  # Exemple de tableau de 6 valeurs de vitesse
        rospy.loginfo(f"Publishing joint velocities: {velocities.data}")
        pub.publish(velocities)
        rate.sleep()

if __name__ == '__main__':
    try:
        joint_velocity_publisher()
    except rospy.ROSInterruptException:
        pass
