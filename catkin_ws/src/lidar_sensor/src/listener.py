#! /usr/bin/env python
import rospy
from duckietown_msgs.msg import lidar_9
from sensor_msgs.msg import LaserScan

def rads(angle):
		angle_rad =  (angle*2*3.1416)/360    #transforma de angulos a radianes
		return angle_rad
def mm_to_metters(distance):
	return distance/1000.0

class LidarProccesing(object):
	
	def __init__(self):
		self.pub=rospy.Publisher('/lidar_rviz/',  LaserScan , queue_size=1)
		self.subs=rospy.Subscriber('lidarTopic',lidar_9, self.callback)
		self.laser = LaserScan()
		self.laser.angle_increment = rads(10)          
		self.laser.angle_max = rads(-90)  #grados 
		self.laser.angle_min = rads(90)    #angulo en grados
		self.laser.time_increment = (15)/1000
		self.laser.scan_time = (15*18)/1000 #en milisegundos 
		self.laser.range_min = 0
		self.laser.range_max = 5
		self.laser.header.frame_id="mapita"

		self.laser.ranges = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	def callback(self, msg):	
		#self.laser.header.seq = rospy.get_time()
		self.laser.header.stamp = rospy.Time.now()
		#print str(msg.angulo/self.laser.angle_increment)
		print mm_to_metters(msg.distancia)
		print str((msg.angulo/10) -1)
		self.laser.ranges[ (msg.angulo/10) -1] = mm_to_metters(msg.distancia)		
		
		self.pub.publish(self.laser)
		
def main():
	#pub = rospy.Publisher('LidarRadarTopic' , LaserScan, queue_size=1)
	rospy.init_node('main',anonymous = True) #es para que el programa reconozca un unico nodo llamado listener y evitar confusines
	obj = LidarProccesing()
	rospy.spin()
	

if __name__ == '__main__':
	main()