# Core2-Task3: ROS 2 Talker and Subscriber

This repository contains a basic ROS 2 implementation of a chatter system featuring a **Talker (Publisher)** and a **Listener (Subscriber)** node written in Python. 

## Repository Contents

*   **`talker.py`**: A ROS 2 node designed to publish chatter messages to a specific topic.
*   **`listener.py`**: A ROS 2 node designed to subscribe to the chatter topic and log incoming messages.

> **Note:** The functional code within `talker.py` and `listener.py` is commented out. 

## Prerequisites

To run these nodes, you need:
*   An installed distribution of **ROS 2** (e.g., Humble, Jazzy)
*   Python 3

## How to Use

1. **Clone the repository** into your ROS 2 workspace source directory (`dev_ws/src`):
   ```bash
   git clone git@github.com:Joajibola/Core2-Task3.git
