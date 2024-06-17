// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dsr_msgs2:srv/GetCurrentTool.idl
// generated code does not contain a copyright notice

#ifndef DSR_MSGS2__SRV__DETAIL__GET_CURRENT_TOOL__STRUCT_H_
#define DSR_MSGS2__SRV__DETAIL__GET_CURRENT_TOOL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetCurrentTool in the package dsr_msgs2.
typedef struct dsr_msgs2__srv__GetCurrentTool_Request
{
  uint8_t structure_needs_at_least_one_member;
} dsr_msgs2__srv__GetCurrentTool_Request;

// Struct for a sequence of dsr_msgs2__srv__GetCurrentTool_Request.
typedef struct dsr_msgs2__srv__GetCurrentTool_Request__Sequence
{
  dsr_msgs2__srv__GetCurrentTool_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dsr_msgs2__srv__GetCurrentTool_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetCurrentTool in the package dsr_msgs2.
typedef struct dsr_msgs2__srv__GetCurrentTool_Response
{
  /// tool name
  rosidl_runtime_c__String info;
  bool success;
} dsr_msgs2__srv__GetCurrentTool_Response;

// Struct for a sequence of dsr_msgs2__srv__GetCurrentTool_Response.
typedef struct dsr_msgs2__srv__GetCurrentTool_Response__Sequence
{
  dsr_msgs2__srv__GetCurrentTool_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dsr_msgs2__srv__GetCurrentTool_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DSR_MSGS2__SRV__DETAIL__GET_CURRENT_TOOL__STRUCT_H_