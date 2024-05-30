#!/bin/bash

# Autoriser les connexions locales X11
xhost +local:root

# Démarrer le conteneur Docker avec support X11
docker run -it --rm --name doosan_robot_container \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    --device=/dev/dri:/dev/dri \
    ros:noetic /bin/bash