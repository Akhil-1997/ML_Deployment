# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Dash app will run
EXPOSE 8050

# Command to run the Dash app
CMD ["python", "dash_app.py"]
