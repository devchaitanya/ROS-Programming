#!/usr/bin/env python
# Packet Publisher
import rospy
from std_msgs.msg import String

rospy.init_node('packet_publisher')
packet_pub = rospy.Publisher('packet_name', String, queue_size=10)

rate = rospy.Rate(1) # 1 Hz

while not rospy.is_shutdown():
    packet_name = "VITCC"
    packet_pub.publish(packet_name)
    rospy.loginfo("Packet name: %s", packet_name)
    rate.sleep()
