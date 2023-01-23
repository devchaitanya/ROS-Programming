#!/usr/bin/env python
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# initialize the node
rospy.init_node('draw_square')

# create a publisher to send velocity commands to turtlesim
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# set the rate at which velocity commands will be sent
rate = rospy.Rate(10) # 10 Hz

# create a Twist message to hold the velocity commands
velocity = Twist()

# set the distance turtle will move before turning
distance = 2

# set the angle turtle will turn
angle = 90

# set the speed at which turtle will move
speed = 2

#while not rospy.is_shutdown(): //if you want to move it continuously in square shape
for i in range(5):
    # move forward
    velocity.linear.x = speed
    velocity.angular.z = 0.0
    pub.publish(velocity)
    rate.sleep()
    rospy.sleep(1)
    print("move")
    # rotate to the desired angle
    velocity.linear.x = 0.0
    velocity.angular.z = math.radians(angle)
    pub.publish(velocity)
    #rate.sleep()
    rospy.sleep(2)
    print("turn")

# stop the turtle
velocity.linear.x = 0.0
velocity.angular.z = 0.0
pub.publish(velocity)

