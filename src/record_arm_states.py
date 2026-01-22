import time
import numpy as np
from a2d_sdk.robot import RobotDds as Robot

if __name__ == "__main__":
    # Initialize the robot
    robot = Robot()
    time.sleep(0.5) #Waiting for resource initialization, receiving message

    # Init gripper position
    gripper_states, _ = robot.gripper_states()
    left_gripper = gripper_states[0]
    right_gripper = gripper_states[1]
    # robot.move_gripper([left_gripper, right_gripper])

    position_list = []
    # filename = "movement_records/arm_move_grab_chip_1.npy"
    # filename = "movement_records/arm_move_grab_100_plus_2.npy"
    # filename = "movement_records/arm_move_grab_small_bottle_3.npy"
    # filename = "movement_records/arm_move_place_chip_left.npy"
    # filename = "movement_records/arm_move_place_chip_right.npy"
    filename = "movement_records/test.npy"
    try:
        while True:
            # NOTE: The gripper angle can be normalized to 0, 1
            user_input = input("Press Enter to record current arm positions, or type gripper command (left_gripper <angle>) OR (right_gripper <angle>)")
            if not user_input:
                arm_pos, timestamp = robot.arm_joint_states() 
                print("Saving arm position: " + str(list(arm_pos)))
                position_list.append({"Command": "Move_arm", "Joint Angles": list(arm_pos)})
            elif user_input.split(" ")[0] == "left_gripper":
                left_gripper = float(user_input.split(" ")[1])
                print("Saving left gripper angle: " + str(left_gripper))
                robot.move_gripper([left_gripper, right_gripper])
                position_list.append({"Command": "Move_left_gripper", "Gripper Angle": left_gripper})
            elif user_input.split(" ")[0] == "right_gripper":
                right_gripper = float(user_input.split(" ")[1])
                print("Saving right gripper angle: " + str(right_gripper))
                robot.move_gripper([left_gripper, right_gripper])
                position_list.append({"Command": "Move_right_gripper", "Gripper Angle": right_gripper})
            else:
                break

        position_arr = np.array(position_list)

        np.save(filename, position_arr)
        robot.shutdown()

    except KeyboardInterrupt:
        np.save(filename, position_arr)
        robot.shutdown()