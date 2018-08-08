#! /usr/bin/env python

from duckietown_msgs.msg import lidar_9
import rospy


angle_increment = 10          
angle_max = 180  #grados 
angle_min = 0    #angulo en grados

def rads(angle):
	angle_rad =  (angle*2*3.1416)/360    #transforma de angulos a radianes
	return angle_rad

def callback(msg):
	print rads(angle_min)
	print rads(angle_max)
	print rads(angle_increment)
	print rospy.get_time()
	print str(msg.ditancia) 
	print str(msg.angulo)
#	print msg.angulo
#	print msg.ditancia

def listener():
	rospy.init_node('laser_scan_generator',anonymous = True) #es para que el programa reconozca un unico nodo llamado listener y evitar confusines
	rospy.Subscriber('lidarTopic',lidar_9, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
