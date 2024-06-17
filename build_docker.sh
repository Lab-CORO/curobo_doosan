#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <ROS_DISTRO>"
  exit 1
fi

ROS_DISTRO=$1

docker build -t ros:$ROS_DISTRO -f ${ROS_DISTRO}.dockerfile .
