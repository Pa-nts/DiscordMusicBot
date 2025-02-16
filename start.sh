#!/bin/bash

# Start Lavalink in the background
java -jar Lavalink.jar &

# Wait for Lavalink to start
sleep 5

# Start the Discord bot
python3 "Discord Music Bot.py"
