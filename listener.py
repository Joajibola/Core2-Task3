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
from rclpy.executors import ExternalShutdownException #This import is to handle clean system shutdown
from rclpy.node import Node #imports the node class in order to create a custom subcriber node

from std_msgs.msg import String # Import string message type, which will be used to send text over the network


class Listener(Node): #Defines new class listener inherits from NODE

    #initialization method which runs as we create the object
    def __init__(self):
        super().__init__('listener')
        #This creates a listener connection and saves it as self.sub , it listenes for only stringmessages on the chatter, and the self.chatter_callback runs only when a message arrives
        self.sub = self.create_subscription(String, 'chatter', self.chatter_callback, 10) #This line set up a listener connection, saves it as self.sub 

    #This function only triggers when a message arrives
    def chatter_callback(self, msg):
        self.get_logger().info('I heard: [%s]' % msg.data) # msg.data: Reaches inside the incoming ROS String container to pull out the raw text.
        # self.get_logger().info() prints a styled, timestamped log directly to the terminal screen.
        # '%s' acts as a placeholder that gets filled with the contents of msg.data.


def main(args=None):
    rclpy.init(args=args)

    node = Listener() # initiates the listeners class which establishes the subscription network connection
    
    #Uses a try except and finally block to control the execution
    
    try:
        rclpy.spin(node) # Puts the script into an infinite loop. 
    except (KeyboardInterrupt, ExternalShutdownException): 
        pass # If the Ctrl+C (KeyboardInterrupt) is pressed, ignore the error and pass silently
    finally:
        node.destroy_node() 
        rclpy.try_shutdown() #shutdown the ros2 network connection for this process


# Check if this script is being run directly from the terminal
if __name__ == '__main__':
    main() #Calls the main function to run the entire program
