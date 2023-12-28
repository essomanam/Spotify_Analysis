# Use the official Python image with version 3.10
FROM python:3.10

# Create the /app directory
RUN mkdir /app

# Install rsync
RUN apt-get update && apt-get install -y rsync

# Copy the contents of the current directory to /app in the image
COPY . /app/

# Use rsync to exclude certain files/directories
RUN rsync -a --exclude=data --exclude=__pycache__ --exclude=venv /app/ /app/

# Set the working directory to /app
WORKDIR /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set the FLASK_APP environment variable
ENV FLASK_APP=main.py

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
