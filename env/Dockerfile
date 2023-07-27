# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /src

# Install system packages required by the Quantum Thruster Simulation software
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


# Use a smaller parent image
FROM python:3.8-slim-buster as runtime

# Set the working directory in the container
WORKDIR /app

# Copy over the built wheels from the builder stage
COPY --from=builder /wheels /wheels

# Install the Python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r /wheels/requirements.txt \
    && rm -rf /wheels

# Add metadata to the image to describe which port the container is listening on at runtime
EXPOSE 80

# Copy the rest of the current directory contents into the container at /app
COPY . /app

# Run main.py when the container launches
CMD ["python", "src/main.py"]
