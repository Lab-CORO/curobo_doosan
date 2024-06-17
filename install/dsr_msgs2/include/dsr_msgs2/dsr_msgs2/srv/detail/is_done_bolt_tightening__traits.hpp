// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dsr_msgs2:srv/IsDoneBoltTightening.idl
// generated code does not contain a copyright notice

#ifndef DSR_MSGS2__SRV__DETAIL__IS_DONE_BOLT_TIGHTENING__TRAITS_HPP_
#define DSR_MSGS2__SRV__DETAIL__IS_DONE_BOLT_TIGHTENING__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dsr_msgs2/srv/detail/is_done_bolt_tightening__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dsr_msgs2
{

namespace srv
{

inline void to_flow_style_yaml(
  const IsDoneBoltTightening_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: m
  {
    out << "m: ";
    rosidl_generator_traits::value_to_yaml(msg.m, out);
    out << ", ";
  }

  // member: timeout
  {
    out << "timeout: ";
    rosidl_generator_traits::value_to_yaml(msg.timeout, out);
    out << ", ";
  }

  // member: axis
  {
    out << "axis: ";
    rosidl_generator_traits::value_to_yaml(msg.axis, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IsDoneBoltTightening_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: m
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m: ";
    rosidl_generator_traits::value_to_yaml(msg.m, out);
    out << "\n";
  }

  // member: timeout
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timeout: ";
    rosidl_generator_traits::value_to_yaml(msg.timeout, out);
    out << "\n";
  }

  // member: axis
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "axis: ";
    rosidl_generator_traits::value_to_yaml(msg.axis, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IsDoneBoltTightening_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dsr_msgs2

namespace rosidl_generator_traits
{

[[deprecated("use dsr_msgs2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dsr_msgs2::srv::IsDoneBoltTightening_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  dsr_msgs2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dsr_msgs2::srv::to_yaml() instead")]]
inline std::string to_yaml(const dsr_msgs2::srv::IsDoneBoltTightening_Request & msg)
{
  return dsr_msgs2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dsr_msgs2::srv::IsDoneBoltTightening_Request>()
{
  return "dsr_msgs2::srv::IsDoneBoltTightening_Request";
}

template<>
inline const char * name<dsr_msgs2::srv::IsDoneBoltTightening_Request>()
{
  return "dsr_msgs2/srv/IsDoneBoltTightening_Request";
}

template<>
struct has_fixed_size<dsr_msgs2::srv::IsDoneBoltTightening_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<dsr_msgs2::srv::IsDoneBoltTightening_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<dsr_msgs2::srv::IsDoneBoltTightening_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace dsr_msgs2
{

namespace srv
{

inline void to_flow_style_yaml(
  const IsDoneBoltTightening_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IsDoneBoltTightening_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IsDoneBoltTightening_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dsr_msgs2

namespace rosidl_generator_traits
{

[[deprecated("use dsr_msgs2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dsr_msgs2::srv::IsDoneBoltTightening_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  dsr_msgs2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dsr_msgs2::srv::to_yaml() instead")]]
inline std::string to_yaml(const dsr_msgs2::srv::IsDoneBoltTightening_Response & msg)
{
  return dsr_msgs2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dsr_msgs2::srv::IsDoneBoltTightening_Response>()
{
  return "dsr_msgs2::srv::IsDoneBoltTightening_Response";
}

template<>
inline const char * name<dsr_msgs2::srv::IsDoneBoltTightening_Response>()
{
  return "dsr_msgs2/srv/IsDoneBoltTightening_Response";
}

template<>
struct has_fixed_size<dsr_msgs2::srv::IsDoneBoltTightening_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<dsr_msgs2::srv::IsDoneBoltTightening_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<dsr_msgs2::srv::IsDoneBoltTightening_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<dsr_msgs2::srv::IsDoneBoltTightening>()
{
  return "dsr_msgs2::srv::IsDoneBoltTightening";
}

template<>
inline const char * name<dsr_msgs2::srv::IsDoneBoltTightening>()
{
  return "dsr_msgs2/srv/IsDoneBoltTightening";
}

template<>
struct has_fixed_size<dsr_msgs2::srv::IsDoneBoltTightening>
  : std::integral_constant<
    bool,
    has_fixed_size<dsr_msgs2::srv::IsDoneBoltTightening_Request>::value &&
    has_fixed_size<dsr_msgs2::srv::IsDoneBoltTightening_Response>::value
  >
{
};

template<>
struct has_bounded_size<dsr_msgs2::srv::IsDoneBoltTightening>
  : std::integral_constant<
    bool,
    has_bounded_size<dsr_msgs2::srv::IsDoneBoltTightening_Request>::value &&
    has_bounded_size<dsr_msgs2::srv::IsDoneBoltTightening_Response>::value
  >
{
};

template<>
struct is_service<dsr_msgs2::srv::IsDoneBoltTightening>
  : std::true_type
{
};

template<>
struct is_service_request<dsr_msgs2::srv::IsDoneBoltTightening_Request>
  : std::true_type
{
};

template<>
struct is_service_response<dsr_msgs2::srv::IsDoneBoltTightening_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DSR_MSGS2__SRV__DETAIL__IS_DONE_BOLT_TIGHTENING__TRAITS_HPP_