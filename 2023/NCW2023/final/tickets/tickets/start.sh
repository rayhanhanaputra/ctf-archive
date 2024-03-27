#!/bin/bash

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
logfile="logs/server_${timestamp}.txt"

while [ true ]
do
    echo "Stopping docker..."
    docker compose down
    docker volume rm tickets_db_data
    docker volume rm tickets_wp_data
    docker-compose up --build&>> "$logfile" &
    echo "Docker Started... waiting for 15 minutes"
    sleep 900
done