#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image 
import cv2
import numpy as np
from cv_bridge import CvBridge
from geometry_msgs.msg import Point

class Detect(object):
	
	def __init__(self, args):
		super(Detect, self).__init__()
		self.args = args
        	self.publisher = rospy.Publisher("/duckiebot/Yo_solo_hago_un_cuadradito_al_rededor_de_alguna_wea_amarilla", Image, queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/camera_node/image/raw", Image, self.callback)
		self.publisher2 = rospy.Publisher("/duckiebot/Hola",Image, queue_size=10)
		self.publisher3 = rospy.Publisher("/duckiebot/PatoUbicacion", Point, queue_size=10)
		#self.publisher3 = rospy.Publisher("/duckiebot/Coordenadas", ,)
		self.image = Image()
		self.bridge = CvBridge()

	def callback(self,msg):
		aa = 20
		bb = 20
		AnchoPato = 15
		fx = 0.1
		fy = 0.1
		cx = 0.1
		cy = 0.1
		img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		imageout = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(imageout,np.array([0,210,100]),np.array([30,255,200]))
		kernel = np.ones((5,5),np.uint8)
		img_out = cv2.erode(mask,kernel,iterations = 1)
		img_out = cv2.dilate(mask,kernel,iterations = 2)
		image_out = cv2.bitwise_and(img, img, mask = img_out)
		hola, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		areas = [cv2.contourArea(c) for c in contours] #Busca todos los rectangulos en la imagen
		for a in areas:
			index = areas.index(a)
			cnt = contours[index]  #Denomina cnt a los bordes del rectangulo de mayor area
			if areas[index] < 200 or areas[index] > 3000: #and hierarchy[index] == 0:
				continue
			else:
				x,y,w,h = cv2.boundingRect(cnt)
				cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
				if w<aa or h<bb:
					None
				else:
					z = (fx * AnchoPato)/w
					u = x + (w/2)
					v = y + (h/2)
					UbP = ((u-z*cx)/fx, (z-z*cy)/fy, z)
					self.publisher3.publish(UbP)
				print "w = ", w, "h = ", h, "area = ", a
		image = self.bridge.cv2_to_imgmsg(img,"bgr8")
		self.publisher.publish(image)
		image_out = self.bridge.cv2_to_imgmsg(image_out,"bgr8")
		self.publisher2.publish(image_out)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Detect('args') # Crea un objeto del tipo Controller, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
