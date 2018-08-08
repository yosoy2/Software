#! /usr/bin/env python

import rospy
from duckietown_msgs.msg import lidar_9
from duckietown_msgs.msg import laserScan_1

angle_increment = 10          
angle_max = 180  #grados 
angle_min = 0    #angulo en grados
timeIncrement = 15;
scanTime = (15*18*2) #en milisegundos 
rangeMin a
rangeMax = b

def rads(angle):
	angle_rad =  (angle*2*3.1416)/360    #transforma de angulos a radianes
	return angle_rad

def callback(msg):
#	msg = lidar_9()
#	listaDistancias = []
#	listaIndices = []
#	posicionAngulo=msg.angulo/angle_increment
#	listaDistancias.append(msg.distancia)		
	print msg.angulo
	print msg.distancia
	print rads(angle_min)
	print rads(angle_max)
	print rads(angle_increment)
	print rospy.get_time()
	print timeIncrement
	print scanTime
	print rangeMax
	print rangeMin
#	print str(msg.ditancia) + str(msg.angulo)
#	print msg.angulo
#	print msg.ditancia
	return [msg.distancia,msg.angulo,rads(angle_min),rads(angle_max),rads(angle_increment),timeIncrement,scanTime,rangeMin,rangeMax]

def main():
	pub=rospy.Publisher('topic',  laserScan_1 , quque_size=1)
#	print("nodo creada con exito")
	rospy.init_node('main',anonymous = True) #es para que el programa reconozca un unico nodo llamado listener y evitar confusines
	rospy.Subscriber('lidarTopic',lidar_9, callback)
	rospy.spin() #esto es para que se repita y no pare con el control c
	rate = rospy.Rate(1)
	mensaje = lidar_9()
	while rospy.is_shutdown():
		mensaje.angle_min = callback(msg)[2]
		mensaje.angle_max = callback(msg)[3]
		mensaje.angle_increment = callback(msg)[4]
		mensaje.time_increment = callback(msg)[5]
		mensaje.scan_time = callback(msg)[6]
		mensaje.range_min = callback(msg)[7]
		mensaje.range_max = callback(msg)[8]
		listaDistancias = []
		while len(listaDistancias)<=18:
			listaDistancias.append(callback(msg)[0])
		  	else:
		  		mensaje.ranges = listaDistancias
		  		pub.Publish(mensaje)
		  		rate.sleep()


if __name__ == '__main__':
	main()