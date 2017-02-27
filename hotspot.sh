#!/usr/bin/env bash
# This file enables/disables a hotspot named 'vehicle_name-wifi'

# if the vehicle name is not set, exit
if [ -z "$VEHICLE_NAME" ]; then
  echo "VEHICLE_NAME is not set. Please run 'source set_vehicle_name.sh' script before enabling the hotspot"
  exit

# if the vehicle name is set but no hotspot is active, enable the hotspot
else 
  if [ -z "$HOTSPOT" ]; then
    # vehicle name is set, create hotspot-ssid variable
    export HOTSPOT="$VEHICLE_NAME-wifi"

    echo "Enabling hotspot $HOTSPOT..."
    nmcli device wifi hotspot con-name $HOTSPOT ssid $HOTSPOT band bg password quackquack
    echo "$HOTSPOT enabled."

    # if the hotspot variable exists, we considered it as active, so we disable it
  else
    echo "Disabling hotspot $HOTSPOT..."
    nmcli connection down $HOTSPOT
    unset HOTSPOT
    echo "$HOTSPOT disabled."
  fi
fi
