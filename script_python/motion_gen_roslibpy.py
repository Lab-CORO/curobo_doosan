import sys
import os

venv_path = '/pkgs/curobo/try/lib/python3.8/site-packages'
sys.path.append(venv_path)

import roslibpy

# Initialisation de la connexion ROS
ros_client = roslibpy.Ros(host='localhost', port=9090)  # Remplace 'localhost' par l'adresse de ton broker ROS si nécessaire
ros_client.run()

trajectory_pub = roslibpy.Topic(ros_client, '/trajectory', 'your_trajectory_message_type')  # Remplace 'your_trajectory_message_type' par le type de message approprié

print(roslibpy.__version__)

from curobo.wrap.reacher.mpc import MpcSolver, MpcSolverConfig
from curobo.types.state import JointState
from curobo.rollout.rollout_base import Goal

# Configuration de l'environnement
world_config = {
    "cuboid": {
        "table": {"dims": [2, 2, 0.2], "pose": [0.4, 0.0, -0.1, 1, 0, 0, 0]},
        "cube_1": {"dims": [0.1, 0.1, 0.2], "pose": [0.4, 0.0, 0.5, 1, 0, 0, 0]},
    },
    "mesh": {
        "scene": {
            "pose": [1.5, 0.080, 1.6, 0.043, -0.471, 0.284, 0.834],
            "file_path": "scene/nvblox/srl_ur10_bins.obj",
        }
    },
}

mpc_config = MpcSolverConfig.load_from_robot_config(
    "/pkgs/curobo_doosan/src/m1013/m1013.yml",
    world_config,
    store_rollouts=True,
    step_dt=0.03,
)
mpc = MpcSolver(mpc_config)

retract_cfg = mpc.rollout_fn.dynamics_model.retract_config.clone().unsqueeze(0)
kinematics_state = mpc.rollout_fn.compute_kinematics(
    JointState.from_position(retract_cfg + 0.5, joint_names=mpc.joint_names)
)
goal_pose = kinematics_state.ee_pose.clone()

start_state = JointState.from_position(retract_cfg, joint_names=mpc.joint_names)
print("Successfully loaded Doosan M1013")

goal = Goal(
    current_state=start_state,
    goal_state=JointState.from_position(retract_cfg, joint_names=mpc.joint_names),
    goal_pose=goal_pose,
)

goal_buffer = mpc.setup_solve_single(goal, 1)
mpc.update_goal(goal_buffer)

i = 0
while True and i < 100:  # Boucle de contrôle
    current_state = start_state
    result = mpc.step(current_state)

    # Publier la commande sur le topic ROS
    command = result.action
    trajectory_pub.publish({'velocity': command.velocity.tolist()})

    print(result.metrics.pose_error.item())
    print(f"Consignes de vitesse : {command.velocity.tolist()}")

    start_state = command
    i += 1

# Arrêtez le client ROS
ros_client.terminate()
