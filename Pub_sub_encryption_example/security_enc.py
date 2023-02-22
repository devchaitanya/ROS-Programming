#!/usr/bin/env python
# Security Publisher
import rospy
from std_msgs.msg import String

def security_publisher(data):
    pub = rospy.Publisher('encr', String, queue_size=10)
    rospy.init_node('security_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1 Hz
    while not rospy.is_shutdown():
        packet = data.data
        encrypted_packet = ""
        for char in packet:
            encrypted_packet += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        rospy.loginfo(encrypted_packet)
        pub.publish(encrypted_packet)
        rate.sleep()

def packet_callback(data):
    security_publisher(data)

if __name__ == '__main__':
    rospy.init_node('security_publisher', anonymous=True)
    rospy.Subscriber("packet_name", String, packet_callback)
    rospy.spin()
