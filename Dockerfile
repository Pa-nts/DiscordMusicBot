# Use Python 3.10 as base image
FROM python:3.10

# Install Java for Lavalink
RUN apt update && apt install -y openjdk-17-jdk

# Set the working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install required Python packages (if you have a requirements.txt)
RUN pip install -r requirements.txt

# Expose Lavalink's default port
EXPOSE 2333

# Start Lavalink and the bot
CMD java -jar Lavalink.jar & sleep 5 && python "Discord Music Bot.py"
