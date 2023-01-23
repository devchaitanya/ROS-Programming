#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    # Initialize a new node
    rospy.init_node('publisher1_node', anonymous=True)
    # Create a publisher object that will publish to the 'CSE3102' topic
    pub = rospy.Publisher('CSE3102', String, queue_size=10)
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)

    # Continue running until the node is shut down
    while not rospy.is_shutdown():
        _string = "/CSE3102"
        # Log the message string
        rospy.loginfo(_string)
        # Publish the message string to the 'CSE3102' topic
        pub.publish(_string)
        # Sleep for the duration of 1/rate
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

