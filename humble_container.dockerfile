FROM osrf/ros:humble-desktop-full


ENV ROS_DISTRO=humble
ENV ROS_ROOT=/opt/ros/$ROS_DISTRO
ENV ROS_PACKAGE_PATH=/opt/ros/$ROS_DISTRO/share

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    nano \
    && rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO humble

RUN mkdir -p /humble_ws/src && cd humble_ws/src

COPY velocity_pub /humble_ws/src/velocity_pub

WORKDIR /humble_ws

RUN /bin/bash -c '. /opt/ros/$ROS_DISTRO/setup.bash'

RUN apt-get update && apt-get install -y \
    wget \
    python3-rosdep

RUN /bin/bash -c '. /opt/ros/$ROS_DISTRO/setup.bash; \
                  colcon build --symlink-install'

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc
RUN echo "source /humble_ws/install/setup.bash" >> /root/.bashrc

RUN wget https://download.jetbrains.com/python/pycharm-community-2021.3.3.tar.gz \
    && tar -xzf pycharm-community-2021.3.3.tar.gz -C /opt/ \
    && rm pycharm-community-2021.3.3.tar.gz

ENV PYCHARM_HOME /opt/pycharm-community-2021.3.3
ENV PATH $PYCHARM_HOME/bin:$PATH

RUN echo '#!/bin/bash\n/opt/pycharm-community-2021.3.3/bin/pycharm.sh "$@"' > /usr/local/bin/pycharm && chmod +x /usr/local/bin/pycharm

RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -

    RUN add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    
    RUN apt-get update && apt-get install -y code
    
    RUN echo "alias code='code --no-sandbox --user-data-dir=/root/.vscode-root'" >> /root/.bashrc

CMD ["bash"]