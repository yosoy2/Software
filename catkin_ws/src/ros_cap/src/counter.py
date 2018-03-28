#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

class Publisher():
    def __init__(self):
        self.publisher = rospy.Publisher('counter', Int32, queue_size=10)
        self.counter = 0

    def publish(self):
        self.publisher.publish(Int32(self.counter))
        self.counter += 1


if __name__ == '__main__':
    publisher = Publisher()
    rospy.init_node('counter_publisher')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        publisher.publish()
        rate.sleep()
