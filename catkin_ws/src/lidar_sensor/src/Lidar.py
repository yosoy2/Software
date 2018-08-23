#!/usr/bin/env python
# autores: Pedro y Tomas

import rospy
#porno
from duckietown_msgs.msg import Twist2DStamped
from duckietown_msgs.msg import Lidar

from geometry_msgs.msg import Point
from sensor_msgs.msg import Joy

# La clase Controller reune la informacion de joy y lidarTopic con el
# fin de entregar un seguro para la prevencion de colisiones del
# Duckiebot.
class Controller(object):
    def __init__(self, args):
        super(Controller, self).__init__()
        
        self.args = args
        
        self.publisher = rospy.Publisher(
            "/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped,
            queue_size=10)
        
        self.subscriberJoy = rospy.Subscriber("/duckiebot/joy", Joy,
            self.LecturaJoy)
        self.subscriberLidar = rospy.Subscriber("/duckiebot/lidarTopic",
            Lidar, self.LecturaLidar)
        
        self.twist = Twist2DStamped()

        self.anguloGiro = 10
        self.list = [0]*n


    def LecturaJoy(self,msg):
        self.v = msg.axes[1]*(-1)
        self.omega = msg.axes[3]
        if(msg.buttons[1]):
            self.twist.v = 0
            self.twist.omega = 0

    
        
    def LecturaLidar(self,msg):
        # Definicion de variables.
        n = (msg.anglMax-msg.anglMin)/msg.anglDelta + 1
        tiempoBarrido = ((msg.anglMax-msg.anglMin)/msg.anglDelta)
            * msg.tiempo
        velocidadMaxima = 250
        indiceDato = (msg.angulo-msg.anglMin)/msg.anglDelta
        

        # Creacion de la lista de distancias.
        if self.list is not None:
            L = self.list


        # Actualizacion de lista de distancias.
        if self.twist.omega == 0:
            for i in range(L):
                L[i] = L[i] + self.twist.v * 0.015     
        else:
            self.anguloGiro = self.anguloGiro + self.twist.omega
            if int(anguloGiro) == 1:
                L = L.pop(n).append(0)
                self.anguloGiro = 0
            elif int(anguloGiro) == -1:
                L = L.pop(1).reverse().append(0).reverse()
                self.anguloGiro = 0


        # Actualizar datos de distancia.        
        L[indiceDato] = msg.distancia + self.twist.v * msg.anglDelta 
        

        # Distancia de objeto mas cercano.
        indicesCentral = (msg.anglMax - msg.anglMin)/(2 * msg.anglDelta)
        G = []
        for indice > indiceCentral - 3 and indice < indiceCentral + 3:
            G[indice] = L[indice]
        distanciaMin = min(i in G)


        # Freno anticolisiones.
        if distanciaMin <= V * T:
            self.twist.v = 0


        self.publisher.publish(self.twist)
        self.list = L

        
def main():
    rospy.init_node('test')

    obj = Controller('args')

    rospy.spin()


if __name__ =='__main__':
    main()
