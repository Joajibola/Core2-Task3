# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy #imports the standard ros2 client library for python
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node #imports the node class that provides a structure for the ros2 node

from std_msgs.msg import String # Import string message type, which will be used to send text over the network


class Talker(Node): #This talker class inherits all the propertices form the 'node'

    #initialization method which runs as we create the object
    def __init__(self):
        super().__init__('talker')
        self.i = 0 # internal counter variable to track sent messages
        self.pub = self.create_publisher(String, 'chatter', 10) # Create a Publisher that broadcasts 'String' messages on a topic named 'chatter'
        timer_period = 1.0 # This defines that the timer should wake up exactly one second

        # Creates a background timer that triggers the 'timer_callback' function every second
        self.tmr = self.create_timer(timer_period, self.timer_callback)

    # This function runs automatically every single time the timer alerts (every 1 second) cause timer_period = 1.0
    def timer_callback(self):

        msg = String() # This creates an empty ROS 2 String message object container
        msg.data = 'Hello World: {0}'.format(self.i)
        self.i += 1 # Add 1 to our internal counter for the next message
        self.get_logger().info('Publishing: "{0}"'.format(msg.data)) #This prints the log message here directly to the terminal
        self.pub.publish(msg) # Publishes the finished message into the ROS 2 network


def main(args=None):
    rclpy.init(args=args) # Initializes the underlying ROS 2 communications middleware layer

    node = Talker() # initialiszes the custom  talker class

    #Uses a try except and finally block to control the execution
    try:
        rclpy.spin(node) # Put the script into an infinite loop. 
    except (KeyboardInterrupt, ExternalShutdownException): # If the Ctrl+C (KeyboardInterrupt) is pressed, ignore the error and pass silently
        pass
    finally:
        node.destroy_node() # This is a cleanup block that runs right before the scripts finally closes
        rclpy.try_shutdown() #shutdown the ros2 network connection for this process

# Check if this script is being run directly from the terminal
if __name__ == '__main__':
    main() #Calls the main function to run the entire program
