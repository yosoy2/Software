#!/usr/bin/env python
# autores: eduardo y tomas

import rospy #importar ros para python
 # importar mensajes de ROS tipo String y tipo Int32 # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped

class Controller(object):
	
	def __init__(self, args):
		super(Controller, self).__init__()
		self.args = args
<<<<<<< HEAD
        self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size=10)
=======
          	self.publisher = rospy.Publisher("/duckiebot/Control", Twist2DStamped, queue_size=10)
>>>>>>> 1addf0ff1d2f08c583080962125d99189f572d0d
		self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
		self.twist = Twist2DStamped()
		self.list = []

	def callback(self,msg):
        num = msg.axes[1]
		self.list[i]=msg.distancia		
  		self.twist.v=msg.axes[1]*(-1)
		self.twist.omega=msg.axes[3]*10
		if(msg.buttons[1]):
			self.twist.v=0
			self.twist.omega=0
			self.publisher.publish(self.twist)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Controller('args') # Crea un objeto del tipo Controller, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
