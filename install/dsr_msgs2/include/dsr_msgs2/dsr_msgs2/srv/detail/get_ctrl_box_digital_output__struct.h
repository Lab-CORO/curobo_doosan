// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dsr_msgs2:srv/GetCtrlBoxDigitalOutput.idl
// generated code does not contain a copyright notice

#ifndef DSR_MSGS2__SRV__DETAIL__GET_CTRL_BOX_DIGITAL_OUTPUT__STRUCT_H_
#define DSR_MSGS2__SRV__DETAIL__GET_CTRL_BOX_DIGITAL_OUTPUT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetCtrlBoxDigitalOutput in the package dsr_msgs2.
typedef struct dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request
{
  /// ctrlbox digital output port(1 ~ 16)
  int8_t index;
} dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request;

// Struct for a sequence of dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request.
typedef struct dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request__Sequence
{
  dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/GetCtrlBoxDigitalOutput in the package dsr_msgs2.
typedef struct dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response
{
  /// Current output status (0 : ON, 1 : OFF)
  int8_t value;
  bool success;
} dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response;

// Struct for a sequence of dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response.
typedef struct dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response__Sequence
{
  dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dsr_msgs2__srv__GetCtrlBoxDigitalOutput_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DSR_MSGS2__SRV__DETAIL__GET_CTRL_BOX_DIGITAL_OUTPUT__STRUCT_H_