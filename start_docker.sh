#!/bin/bash
##
## Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
##
## NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
## property and proprietary rights in and to this material, related
## documentation and any modifications thereto. Any use, reproduction,
## disclosure or distribution of this material and related documentation
## without an express license agreement from NVIDIA CORPORATION or
## its affiliates is strictly prohibited.
##

input_arg="$1"

if [ -z "$input_arg" ]; then
    echo "Argument empty, trying to run based on architecture"
    arch=$(uname -m)
    if [ "$arch" == "x86_64" ]; then
        input_arg="x86"
    elif [ "$arch" == "arm64" ]; then
        input_arg="aarch64"
    elif [ "$arch" == "aarch64" ]; then
        input_arg="aarch64"
    fi
fi

if [ "$input_arg" == "x86" ]; then

    docker run --rm -it \
    --privileged \
    -e NVIDIA_DISABLE_REQUIRE=1 \
    -e NVIDIA_DRIVER_CAPABILITIES=all  --device /dev/dri \
    --hostname ros1-docker \
    --add-host ros1-docker:127.0.0.1 \
    --gpus all \
    --network host \
    --env DISPLAY=unix$DISPLAY \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --volume /dev:/dev \
    curobo_docker:$input_arg

elif [ "$input_arg" == "aarch64" ]; then

    docker run --rm -it \
    --privileged \
    --runtime nvidia \
    --hostname ros1-docker \
    --add-host ros1-docker:127.0.0.1 \
    --network host \
    --gpus all \
    --env ROS_HOSTNAME=localhost \
    --env DISPLAY=$DISPLAY \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --volume /dev/input:/dev/input \
    curobo_docker:$input_arg

elif [[ "$input_arg" == *isaac_sim* ]] ; then

    xhost +local:docker

    docker run --name container_$1 --entrypoint bash -it --gpus all \
        -e "ACCEPT_EULA=Y" \
        -e "PRIVACY_CONSENT=Y" \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
        -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
        -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
        -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
        -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
        -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
        -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
        -v ~/docker/isaac-sim/documents:/root/Documents:rw \
        --device /dev/dri \
        --device /dev/bus/usb \
        --device /dev/video0 \
        --device /dev/video1 \
        --device /dev/video2 \
        --device /dev/video3 \
        --device /dev/video4 \
        --device /dev/video5 \
        --device /dev/video6 \
        --device /dev/video7 \
        --privileged \
        --volume shared_volume:/qrobo_shared \
        --network host \
        curobo_docker:$1

else
    echo "Unknown docker"
fi
