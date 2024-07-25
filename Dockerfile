# Step 1: Use the official Python 3.9 image as a parent image
FROM python:3.9-slim

# Step 8: Install the Datadog Agent
RUN apt-get update && apt-get install -y curl gnupg \
    && curl -o /tmp/datadog-signing-key.asc https://keys.datadoghq.com/DATADOG_APT_KEY_CURRENT.public \
    && apt-key add /tmp/datadog-signing-key.asc \
    && sh -c "echo 'deb https://apt.datadoghq.com/ stable 7' > /etc/apt/sources.list.d/datadog.list" \
    && apt-get update \
    && apt-get install -y datadog-agent

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the dependencies file to the working directory
COPY requirements.txt .

# Step 4: Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the content of the local directory to the working directory
COPY . .

# Step 6: Make port 8080 available to the world outside this container
EXPOSE 8080

COPY start_uvicorn.sh /app/start_uvicorn.sh

# Make the entrypoint script executable
RUN chmod +x /app/start_uvicorn.sh

# Step 7: Run the application
ENTRYPOINT ["/app/start_uvicorn.sh"]