# Use Python 3.10 as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install required Python packages (if you have a requirements.txt)
RUN pip install -r requirements.txt

# Expose the port for your bot (this may be optional, depending on your setup)
# EXPOSE 8080  # You can add the port if needed, or just remove this line if not required.

# Start the bot
CMD python "Discord Music Bot.py"
