#!/bin/bash

#One time only
DUCKIETOWN_ROOT=$HOME/duckietown
echo export DUCKIETOWN_ROOT=$DUCKIETOWN_ROOT >> $HOME/.bashrc
echo "source $DUCKIETOWN_ROOT/vehicle_name.sh >/dev/null" >> $HOME/.bashrc
echo "source $DUCKIETOWN_ROOT/environment.sh >/dev/null"  >> $HOME/.bashrc

source $DUCKIETOWN_ROOT/vehicle_name.sh
source $DUCKIETOWN_ROOT/environment.sh
