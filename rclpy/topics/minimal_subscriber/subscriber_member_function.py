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

import rclpy

from std_msgs.msg import String


class MinimalSubscriber:

    def __init__(self, node):
        self.subscription = node.create_subscription(
            String,
            'topic',
            self.listener_callback)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('I heard: [%s]' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_publisher')

    minimal_subscriber = MinimalSubscriber(node)
    minimal_subscriber  # prevent unused variable warning
    while rclpy.ok():
        rclpy.spin_once(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
