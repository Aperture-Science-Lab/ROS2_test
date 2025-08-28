import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/blaze/ros2_ws/src/install/trio_robot_controller'
