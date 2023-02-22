#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

def create_turtle1():
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', Spawn)
    turtle1_x = 1
    turtle1_y = 1
    turtle1_theta = 0
    turtle1_name = "dogobot"
    spawner(turtle1_x, turtle1_y, turtle1_theta, turtle1_name)

def create_turtle2():
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', Spawn)
    turtle2_x = 9.0
    turtle2_y = 9.0
    turtle2_theta = 0
    turtle2_name = "catobot"
    spawner(turtle2_x, turtle2_y, turtle2_theta, turtle2_name)

def move_turtles():
    pub1 = rospy.Publisher('/dogobot/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    twist1 = Twist()
    twist1.linear.x = 1
    twist1.angular.z = 1
    
    pub2 = rospy.Publisher('/catobot/cmd_vel', Twist, queue_size=10)
    twist2 = Twist()
    twist2.linear.x = 1
    twist2.angular.z = -1
    
    while not rospy.is_shutdown():
        pub1.publish(twist1)
        pub2.publish(twist2)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('turtle_spawner')
        create_turtle1()
        create_turtle2()
        move_turtles()
    except rospy.ROSInterruptException:
        pass

