#include <ros/ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64MultiArray.h>
#include <sstream>
#include <vector>
#include <string>
#include <iterator>

class StringToFloat64MultiArray
{
public:
    StringToFloat64MultiArray()
    {
        pub_ = nh_.advertise<std_msgs::Float64MultiArray>("/dsr_joint_velocity_controller/command", 10);
        sub_ = nh_.subscribe("/string_topic", 10, &StringToFloat64MultiArray::callback, this);
    }

    void callback(const std_msgs::String::ConstPtr& msg)
    {
        std::vector<double> float_array;
        std::istringstream iss(msg->data);
        double number;
        while (iss >> number) {
            float_array.push_back(number);
        }

        std_msgs::Float64MultiArray float_msg;
        float_msg.data = float_array;
        pub_.publish(float_msg);
    }

private:
    ros::NodeHandle nh_;
    ros::Publisher pub_;
    ros::Subscriber sub_;
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "string_to_float64_multiarray_node");
    StringToFloat64MultiArray node;
    ros::spin();
    return 0;
}
