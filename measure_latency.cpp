#include <ros/ros.h>
#include <std_msgs/Float64MultiArray.h>

void callback(const std_msgs::Float64MultiArray::ConstPtr& msg)
{
    if (msg->layout.data_offset != 0)
    {
        double sent_time_sec = msg->layout.data_offset;
        ros::Time sent_time(sent_time_sec);
        ros::Time received_time = ros::Time::now();
        ros::Duration latency = received_time - sent_time;

        ROS_INFO("Message sent at: %f", sent_time.toSec());
        ROS_INFO("Message received at: %f", received_time.toSec());
        ROS_INFO("Latency: %f seconds", latency.toSec());
    }
    else
    {
        ROS_WARN("Received message with no timestamp.");
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "measure_latency_node");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("/dsr_joint_velocity_controller/command", 10, callback);
    ros::spin();
    return 0;
}
