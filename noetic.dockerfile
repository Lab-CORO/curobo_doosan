FROM osrf/ros:noetic-desktop-full

USER root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3-pip \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    git \
    sudo \
    wget \
    python3-catkin-tools \
    gpg \
    apt-transport-https \
    software-properties-common \
    openjdk-11-jdk \
    libxext-dev libxrender-dev libxtst-dev \
    ros-noetic-serial \
    ros-noetic-control-toolbox \
    ros-noetic-control-msgs \
    ros-noetic-moveit-commander \
    ros-noetic-moveit-core \
    ros-noetic-interactive-marker-twist-server \
    ros-noetic-moveit-ros-visualization \
    ros-noetic-lms1xx \
    ros-noetic-twist-mux \
    ros-noetic-imu-tools \
    ros-noetic-moveit-servo \
    ros-noetic-robot-localization \
    ros-noetic-moveit-simple-controller-manager \
    ros-noetic-moveit-planners-ompl \
    ros-noetic-moveit-setup-assistant \
    ros-noetic-velocity-controllers \
    ros-noetic-effort-controllers \
    ros-noetic-ros-control \
    ros-noetic-ros-controllers \
    ros-noetic-moveit-fake-controller-manager \
    liborocos-kdl-dev \
    liborocos-kdl1.4 \
    ros-noetic-rqt-controller-manager \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get remove --purge -y ros-noetic-moveit ros-noetic-rviz || true \
    && apt-get install -y ros-noetic-moveit ros-noetic-rviz

RUN wget https://download.jetbrains.com/python/pycharm-community-2021.3.3.tar.gz \
    && tar -xzf pycharm-community-2021.3.3.tar.gz -C /opt/ \
    && rm pycharm-community-2021.3.3.tar.gz

ENV PYCHARM_HOME /opt/pycharm-community-2021.3.3
ENV PATH $PYCHARM_HOME/bin:$PATH

RUN echo '#!/bin/bash\n/opt/pycharm-community-2021.3.3/bin/pycharm.sh "$@"' > /usr/local/bin/pycharm && chmod +x /usr/local/bin/pycharm

WORKDIR /home/catkin_ws

SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/noetic/setup.bash" >> /home/.bashrc

RUN mkdir -p /home/catkin_ws/src \
    && cd /home/catkin_ws/src \
    && git clone https://github.com/ros-industrial/industrial_core.git -b melodic-devel \
    && git clone https://github.com/wjwwood/serial.git \ 
    && git clone https://github.com/ETS-J-Boutin/doosan-robot_RT.git \
    && git clone https://github.com/LuCarpentier92/ros_doosan.git

RUN source /opt/ros/noetic/setup.bash && cd /home/catkin_ws && rosdep install --from-paths src --ignore-src --rosdistro noetic -r -y

RUN rm -rf /home/catkin_ws/build /home/catkin_ws/devel


RUN echo "source /home/catkin_ws/devel/setup.bash" >> /home/.bashrc

EXPOSE 12345

RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -

RUN add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

RUN apt-get update && apt-get install -y code

RUN echo "alias code='code --no-sandbox --user-data-dir=/root/.vscode-root'" >> /root/.bashrc

RUN cd /home/catkin_ws && sudo apt update && sudo apt install iputils-ping && sudo apt install net-tools

WORKDIR /home/catkin_ws/src

RUN catkin_create_pkg interactive_marker rospy std_msgs sensor_msgs geometry_msgs interactive_markers 

RUN mkdir -p interactive_marker/scripts

COPY interactive_marker.py /home/catkin_ws/src/interactive_marker/scripts

RUN chmod +x interactive_marker/scripts/interactive_marker.py

RUN mkdir -p /home/catkin_ws/script

COPY launch_robot.sh /home/catkin_ws/script

RUN chmod +x /home/catkin_ws/script/launch_robot.sh

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
    cd /home/catkin_ws && \
    catkin_make"

RUN echo "source /home/catkin_ws/devel/setup.bash" >> /root/.bashrc

WORKDIR /home/catkin_ws/

CMD ["bash"]