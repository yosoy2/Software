#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from duckietown_msgs.msg import  Twist2DStamped, BoolStamped

class DuckieMover():
    def __init__(self):
        self.subscriber = rospy.Subscriber('/counter', Int32, self.counter_callback)
        self.publisher = rospy.Publisher('/duckiebot/wheels_driver_node/car_cmd', Twist2DStamped, queue_size=1)
        self.twist = Twist2DStamped()

    def counter_callback(self,msg):
        rospy.loginfo("Recibo el numero: %i",msg.data)
        self.twist.header.stamp = rospy.get_rostime()
        if msg.data % 2:
          self.twist.v = 0.6
        else:
          self.twist.v = -0.6
        self.publisher.publish(self.twist)

if __name__ == '__main__':

    rospy.init_node('duckie_mover')
    duckie = DuckieMover()
    rospy.spin()
