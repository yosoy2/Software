#!/bin/bash

#One time only
echo export DUCKIETOWN_ROOT=$HOME/duckiebot/duckietown >> $HOME/.bashrc
echo source $DUCKIETOWN_ROOT/vehicle_name.sh >> $HOME/.bashrc
echo source $DUCKIETOWN_ROOT/environment.sh >> $HOME/.bashrc
