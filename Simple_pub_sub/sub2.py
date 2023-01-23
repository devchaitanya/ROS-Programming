#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def this_course(data: str):
    rospy.loginfo("I took %s", data.data)

def listener():
    rospy.init_node('subscriber2_node', anonymous=True)
    rospy.Subscriber("CSE2034", String, this_course)
    rospy.spin()

if __name__ == '__main__':
    listener()

