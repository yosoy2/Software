#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

class Sum():
    def __init__(self):
        self.subscriber = rospy.Subscriber('/counter', Int32, self.counter_callback)
        self.counter = 0

    def counter_callback(self,msg):
        rospy.loginfo("Mi suma actual es: %i", self.counter)
        rospy.loginfo("Recibo el numero: %i",msg.data)
        self.counter += msg.data


if __name__ == '__main__':

    rospy.init_node('sum')
    sum = Sum()
    rospy.spin()

