#!/bin/bash

xhost +local:root


docker run --privileged -p 12345:12345 -it --rm --network host --name humble_container \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    --device=/dev/dri:/dev/dri \
    ros:humble_container /bin/bash