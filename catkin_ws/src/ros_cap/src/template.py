#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist


class Template(object):
	def__init__(self, args):
		super(Template, self).__init__()
		self.args = args


	#def publicar(self):

	#def callback(self,msg):


def main():
	rospy.init_node('test') #creación y registro del nodo!

	obj = Template() # Crea un objeto del tipo Template, cuya definición se encuentra arriba

	#objeto.publicar() #llama al método publicar del objeto obj de tipo Template

	#rospy.spin() #función de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
