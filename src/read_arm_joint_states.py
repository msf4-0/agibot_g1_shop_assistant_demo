import time
from a2d_sdk.robot import RobotDds
robot_dds = RobotDds()
while True:
    arm_joint_states = robot_dds.arm_joint_states()
    print(arm_joint_states)
    time.sleep(1)