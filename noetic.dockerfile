FROM osrf/ros:noetic-desktop-full

USER root

# Mise à jour et installation des dépendances supplémentaires
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
    && rm -rf /var/lib/apt/lists/*

# Installation de PyCharm
RUN wget https://download.jetbrains.com/python/pycharm-community-2021.3.3.tar.gz \
    && tar -xzf pycharm-community-2021.3.3.tar.gz -C /opt/ \
    && rm pycharm-community-2021.3.3.tar.gz

ENV PYCHARM_HOME /opt/pycharm-community-2021.3.3
ENV PATH $PYCHARM_HOME/bin:$PATH

RUN echo '#!/bin/bash\n/opt/pycharm-community-2021.3.3/bin/pycharm.sh "$@"' > /usr/local/bin/pycharm && chmod +x /usr/local/bin/pycharm

# Préparation de l'environnement de travail
WORKDIR /home/catkin_ws

SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/noetic/setup.bash" >> /home/.bashrc

# Création du workspace et clonage des repositories nécessaires
RUN mkdir -p /home/catkin_ws/src \
    && cd /home/catkin_ws/src \
    && git clone -b ros_control_compat https://github.com/BryanStuurman/doosan-robot.git doosan-robot-compat \
    && git clone https://github.com/ros-industrial/industrial_core.git -b melodic-devel \
    && git clone https://github.com/wjwwood/serial.git

# Installation des dépendances avec rosdep
RUN source /opt/ros/noetic/setup.bash && cd /home/catkin_ws && rosdep install --from-paths src --ignore-src --rosdistro noetic -r -y

# Compilation du workspace
RUN source /opt/ros/noetic/setup.bash && cd /home/catkin_ws && catkin_make

# Configuration de l'environnement
RUN echo "source /home/catkin_ws/devel/setup.bash" >> /home/.bashrc

EXPOSE 11311

CMD ["bash"]
