#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

# initialize the node
rospy.init_node('circular_movement')

# create a publisher to send velocity commands to turtlesim
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# set the rate at which velocity commands will be sent
rate = rospy.Rate(20) # 10 Hz

# create a Twist message to hold the velocity commands
velocity = Twist()

while not rospy.is_shutdown():
    # set the linear velocity in the x-axis
    velocity.linear.x = 15.0

    # set the angular velocity in the z-axis
    velocity.angular.z = 10.0

    # publish the velocity commands
    pub.publish(velocity)

    # sleep for the specified amount of time
    rate.sleep()


