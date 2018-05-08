#!/usr/bin/env python
# autores: eduardo y tomas

import rospy #importar ros para python
 # importar mensajes de ROS tipo String y tipo Int32 # importar mensajes de ROS tipo geometry / Twist
import controller.py
from duckietown_msgs.msg import Twist2DStamped
from geometry_msgs.msg import Point

class Movimiento(object):
	
	def __init__(self, args):
		super(Movimiento, self).__init__()
		self.args = args
          	self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/Control", Twist2DStamped, self.callback)
		self.suscriber2 = rospy.Subscriber("/duckiebot/PatoUbicacion", Point, self.callback)
		self.twist = Twist2DStamped()

	def callback(self,msg):
		distanciaminima = 20
		posicionXvehiculo = 0
		anchovehiculo  = 300
		g = posicionXvehiculo - self.point.x
		if self.Point.z < distanciaminima and (self.Point.x < -g or self.point.x > g):
			self.twist.v = 0
			self.twist.omega = 10
		else:
			None
		self.publisher.publish(self.twist)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Movimiento('args')

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()

