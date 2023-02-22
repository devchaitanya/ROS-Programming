#!/usr/bin/env python
# Subscriber
import rospy
from std_msgs.msg import Int32

packet_count = 0

def count_callback(count_msg):
    global packet_count
    packet_count = count_msg.data

rospy.init_node('subscriber')
count_sub = rospy.Subscriber('packet_count', Int32, count_callback)

while not rospy.is_shutdown():
    if packet_count > 0:
        print("Number of encrypted packets: ", packet_count)
    else:
        rospy.loginfo("Waiting for packet count...")
    rospy.sleep(1)
