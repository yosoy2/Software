#! /usr/bin/env python

import rospy

from duckietown_msgs.msg import lidar_2

def callback(msg):
	print "este es el angulo:" + str(msg.angulo) + "," + "y la distancia:" + str(msg.distancia)

def listener():
	print("subscripcion creada con exito")
	rospy.init_node('listener',anonymous = True) #es para que el programa reconozca un unico nodo llamado listener y evitar confusines
	rospy.Subscriber('lidarTopic',lidar_2, callback)
	rospy.spin() #esto es para que se repita y no pare con el control c

if __name__ == '__main__':
	listener()