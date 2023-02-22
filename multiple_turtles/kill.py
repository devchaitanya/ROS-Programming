#!/usr/bin/env python
import rospy
from turtlesim.srv import Kill

rospy.init_node('remove_turtle_node')

kill_service = rospy.ServiceProxy('/kill', Kill)

kill_service('turtle1')
