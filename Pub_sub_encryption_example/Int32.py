#!/usr/bin/env python
# Int32 Publisher
import rospy
from std_msgs.msg import Int32

rospy.init_node('packet_count_publisher')
count_pub = rospy.Publisher('packet_count', Int32, queue_size=10)

rate = rospy.Rate(1) # 1 Hz

count = 0

while not rospy.is_shutdown():
    count += 1
    count_pub.publish(count)
    rospy.loginfo("Packet count: %d", count)
    rate.sleep()
