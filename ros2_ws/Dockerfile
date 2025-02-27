FROM ros:humble

# Update and install necessary system packages
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-pip \
    ros-humble-cv-bridge \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*

# Optionally install additional Python packages via pip.
# Uncomment or add packages as needed (e.g., tensorflow, torch, etc.)
RUN pip3 install --upgrade pip && \
    pip3 install opencv-python
    # pip3 install tensorflow torch  # Uncomment to install TensorFlow and PyTorch

# Set the working directory
WORKDIR /ros2_ws

# Default command (will be overridden by docker-compose if used)
CMD ["bash"]
