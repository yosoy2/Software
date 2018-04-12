#!/usr/bin/env python
# autores: eduardo y tomas

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy 
from duckietown_msgs.msg import Twist2DStamped


class Controller(object):
	def __init__(self, args):
		super(Controller, self).__init__()
		self.args = args
          	self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/wheels_cmd", Twist2DStamped, queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
		self.twist = Twist2DStamped

	def callback(self,msg):
		num = msg.axes[1] 
		self.twist.v=msg.axes[1]
		self.twist.omega=0.0
		if(msg.buttons[1]):
			rospy.loginfo(num)
			self.publisher.publish(self.twist)
		#while(num<0):
		#	self.publisher(-1)
		#else: self.publisher(1)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Controller('args') # Crea un objeto del tipo Controller, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
