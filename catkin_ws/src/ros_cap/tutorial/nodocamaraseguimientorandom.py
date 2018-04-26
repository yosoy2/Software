#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image 
import cv2
import numpy as np
from cv_bridge import CvBridge

class Detect(object):
	
	def __init__(self, args):
		super(Detect, self).__init__()
		self.args = args
          	self.publisher = rospy.Publisher("/duckiebot/Yo_solo_hago_un_cuadradito_al_rededor_de_alguna_wea_amarilla", Image, queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/camera_node/image/raw", Image, self.callback)
		self.image = Image()
		self.bridge = CvBridge()

	def callback(self,msg):
		img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		imageout = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(imageout,np.array([15,30,200]),np.array([45,255,255]))
		kernel = np.ones((5,5),np.uint8)
		img_out = cv2.erode(mask,kernel,iterations = 2)
		img_out = cv2.dilate(mask,kernel,iterations = 3)
		image_out = cv2.bitwise_and(img, img, mask = img_out)
		hola, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		areas = [cv2.contourArea(c) for c in contours] #Busca todos los rectangulos en la imagen
		for a in areas:
			if a < 1000:
				i = areas.index(a)
				areas.remove(a)
				para_nada_sirvo_pero_aun_asi_doy = contours.pop(i)
			else: None
		for a in areas:
			index = areas.index(a)
			cnt = contours[index]  #Denomina cnt a los bordes del rectangulo de mayor area
			if areas[index] < 350: #and hierarchy[index] == 0:
				cnt = None
			x,y,w,h = cv2.boundingRect(cnt)
			cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
		image = self.bridge.cv2_to_imgmsg(img,"bgr8")
		self.publisher.publish(image)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Detect('args') # Crea un objeto del tipo Controller, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
