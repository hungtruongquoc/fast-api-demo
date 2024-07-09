# Step 1: Use the official Python 3.9 image as a parent image
FROM python:3.9-slim

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

# Step 7: Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]