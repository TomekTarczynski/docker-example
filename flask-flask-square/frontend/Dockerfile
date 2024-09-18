# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Create a virtual environment inside the container
RUN python -m venv .venv

# Ensure pip is up-to-date in the virtual environment
RUN .venv/bin/pip install --upgrade pip --progress-bar=off

# Install dependencies in the virtual environment
RUN .venv/bin/pip install -r requirements.txt --progress-bar=off

# Make sure the virtual environment is activated by default
ENV PATH="/usr/src/app/.venv/bin:$PATH"

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "frontend.py"]
