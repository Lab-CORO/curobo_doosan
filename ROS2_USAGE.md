# Utilisation du package ROS2 curobo_doosan

Ce package ROS2 contient le robot Doosan M1013 avec son fichier URDF et ses fichiers meshes pour une utilisation avec ROS2.

## Installation

1. Clonez ce dépôt dans votre workspace ROS2:
```bash
cd ~/ros2_ws/src
git clone <url_du_repo> curobo_doosan
```

2. Compilez le package:
```bash
cd ~/ros2_ws
colcon build --packages-select curobo_doosan
source install/setup.bash
```

## Utilisation

### Lancer le robot avec RViz et joint_state_publisher_gui

Pour visualiser le robot dans RViz avec la GUI de contrôle des joints:

```bash
ros2 launch curobo_doosan display.launch.py
```

### Options du fichier launch

Le fichier launch accepte plusieurs arguments:

- `gui`: Lance joint_state_publisher_gui si true, sinon joint_state_publisher (default: true)
```bash
ros2 launch curobo_doosan display.launch.py gui:=false
```

- `rviz`: Lance RViz2 si true (default: true)
```bash
ros2 launch curobo_doosan display.launch.py rviz:=false
```

### Exemple: Lancer uniquement robot_state_publisher et joint_state_publisher (sans GUI)

```bash
ros2 launch curobo_doosan display.launch.py gui:=false rviz:=false
```

## Structure du package

```
curobo_doosan/
├── CMakeLists.txt
├── package.xml
├── launch/
│   ├── display.launch.py
│   └── robot.rviz
└── src/
    └── m1013/
        ├── m1013.urdf
        ├── m1013.yml
        └── meshes/
            ├── m1013_collision/
            ├── m1013_white/
            └── m1013_blue/
```

## Topics ROS2

Une fois le launch file exécuté, les topics suivants sont disponibles:

- `/robot_description`: Description URDF du robot
- `/joint_states`: États des joints du robot
- `/tf` et `/tf_static`: Transformations du robot

## Notes

- Le robot possède 6 joints revolute (joint1 à joint6)
- Le fichier URDF inclut les configurations pour Gazebo et ros2_control
- Les meshes sont disponibles en version collision et visuelle (white/blue)
