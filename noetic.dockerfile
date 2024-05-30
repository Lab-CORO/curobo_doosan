FROM ros:noetic

USER root
RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3-pip \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    git \
    sudo \
    wget \
    python3-catkin-tools\
    openjdk-11-jdk \
    libxext-dev libxrender-dev libxtst-dev \
    && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository universe \
    && apt-get update \
    && apt-get install -y \
    ros-noetic-moveit \
    ros-noetic-joint-state-publisher \
    ros-noetic-robot-state-publisher \
    ros-noetic-xacro \
    ros-noetic-gazebo-ros \
    ros-noetic-gazebo-ros-control \
    ros-noetic-controller-manager \
    ros-noetic-urdf \
    ros-noetic-hardware-interface \
    ros-noetic-serial \
    ros-noetic-control-toolbox \
    ros-noetic-control-msgs \
    ros-noetic-joint-state-controller \
    ros-noetic-position-controllers \
    ros-noetic-velocity-controllers \
    ros-noetic-effort-controllers \
    ros-noetic-ros-control \
    ros-noetic-ros-controllers \
    ros-noetic-moveit-commander \
    ros-noetic-moveit-core \
    ros-noetic-interactive-marker-twist-server \
    ros-noetic-lms1xx \
    ros-noetic-twist-mux \
    ros-noetic-imu-tools \
    ros-noetic-robot-localization \
    ros-noetic-joint-state-publisher-gui \
    ros-noetic-moveit-simple-controller-manager \
    liborocos-kdl-dev \
    ros-noetic-moveit-ros-planning \
    liborocos-kdl1.4 \
    ros-noetic-rviz

RUN wget https://download.jetbrains.com/python/pycharm-community-2021.3.3.tar.gz \
    && tar -xzf pycharm-community-2021.3.3.tar.gz -C /opt/ \
    && rm pycharm-community-2021.3.3.tar.gz

ENV PYCHARM_HOME /opt/pycharm-community-2021.3.3
ENV PATH $PYCHARM_HOME/bin:$PATH

RUN echo '#!/bin/bash\n/opt/pycharm-community-2021.3.3/bin/pycharm.sh "$@"' > /usr/local/bin/pycharm && chmod +x /usr/local/bin/pycharm

WORKDIR /home

SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/noetic/setup.bash" >> /home/.bashrc

RUN mkdir -p /home/ros_ws/src \
    && cd /home/ros_ws/src \
    && git clone -b ros_control_compat https://github.com/BryanStuurman/doosan-robot.git \
    && git clone https://github.com/ros-industrial/industrial_core.git -b melodic-devel

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && cd /home/ros_ws && rosdep install --from-paths src --ignore-src -r -y"

RUN rm -rf /home/ros_ws/build /home/ros_ws/devel \
    && mkdir -p /home/ros_ws/build /home/ros_ws/devel \
    && chmod -R a+rwx /home/ros_ws/build /home/ros_ws/devel

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && cd /home/ros_ws && catkin build"

RUN echo "source /home/ros_ws/devel/setup.bash" >> /home/.bashrc

EXPOSE 11311

RUN apt-get update && apt-get install -y \
    ros-noetic-rviz \
    ros-noetic-rqt-controller-manager
    

CMD ["bash"]
