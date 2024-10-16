#!/bin/bash

echo "Switch Wi-Fi script ran at $(date), V0.2" >> /home/tera/ros2_ws2/Scripts/wifi_run.log

# Network names
preferred_network="Clevon2"
fallback_network="Clevon"

# Check if the preferred network is available
available_network=$(nmcli -t -f SSID dev wifi | grep "^$preferred_network$")

# Function to connect to a network
connect_to_network() {
    local network_name=$1
    echo "Connecting to $network_name..."
    nmcli con up id "$network_name" || echo "Failed to connect to $network_name"
}

if [ -n "$available_network" ]; then
    echo "$preferred_network is available."
    connect_to_network "$preferred_network"
else
    echo "$preferred_network not found, connecting to $fallback_network."
    connect_to_network "$fallback_network"
fi

