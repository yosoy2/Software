#!/bin/bash
source environment.sh
exec roslaunch duckietown joystick.launch veh:=duckiebot
