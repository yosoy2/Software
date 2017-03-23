#!/bin/bash
if [ $# -gt 0 ]; then
	# provided a hostname, use it as ROS_MASTER_URI
	export VEHICLE_NUM=$1
else
	echo "No hostname provided. Using $HOSTNAME."
	export VEHICLE_NUM=x
fi
source set_vehicle_name.sh duckiebot-$VEHICLE_NUM
case $2 in
	on)
		exec bash hotspot.sh on
		;;
	off)
		exec bash hotspot.sh off
		;;
	*)
    	echo "Usage: $0 {num} {on|off}"
    	exit 1
esac
