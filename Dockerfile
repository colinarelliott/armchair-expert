# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the router.py file to the working directory
COPY router.py .

# Expose port 8000
EXPOSE 8000

# Set the command to execute your Python app
CMD ["python", "router.py"]