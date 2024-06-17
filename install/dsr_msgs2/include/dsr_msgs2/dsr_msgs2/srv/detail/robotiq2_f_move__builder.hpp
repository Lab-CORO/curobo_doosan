// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dsr_msgs2:srv/Robotiq2FMove.idl
// generated code does not contain a copyright notice

#ifndef DSR_MSGS2__SRV__DETAIL__ROBOTIQ2_F_MOVE__BUILDER_HPP_
#define DSR_MSGS2__SRV__DETAIL__ROBOTIQ2_F_MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dsr_msgs2/srv/detail/robotiq2_f_move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dsr_msgs2
{

namespace srv
{

namespace builder
{

class Init_Robotiq2FMove_Request_width
{
public:
  Init_Robotiq2FMove_Request_width()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::dsr_msgs2::srv::Robotiq2FMove_Request width(::dsr_msgs2::srv::Robotiq2FMove_Request::_width_type arg)
  {
    msg_.width = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dsr_msgs2::srv::Robotiq2FMove_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dsr_msgs2::srv::Robotiq2FMove_Request>()
{
  return dsr_msgs2::srv::builder::Init_Robotiq2FMove_Request_width();
}

}  // namespace dsr_msgs2


namespace dsr_msgs2
{

namespace srv
{

namespace builder
{

class Init_Robotiq2FMove_Response_success
{
public:
  Init_Robotiq2FMove_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::dsr_msgs2::srv::Robotiq2FMove_Response success(::dsr_msgs2::srv::Robotiq2FMove_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dsr_msgs2::srv::Robotiq2FMove_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dsr_msgs2::srv::Robotiq2FMove_Response>()
{
  return dsr_msgs2::srv::builder::Init_Robotiq2FMove_Response_success();
}

}  // namespace dsr_msgs2

#endif  // DSR_MSGS2__SRV__DETAIL__ROBOTIQ2_F_MOVE__BUILDER_HPP_