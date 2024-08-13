# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir flask requests pymongo

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the tests
CMD ["python", "-m", "unittest", "test_app.py"]
