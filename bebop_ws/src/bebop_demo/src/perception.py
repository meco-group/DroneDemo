#!/usr/bin/env python

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import rospy


class Perception(object):
    '''
    Read out position of the drone, pose of the drone and position of the
    obstacles
    '''

    def __init__(self):
        """
        Initialization of Perception object.
        """
        self.pose_vive = Twist()
        self.pose_bebop = Twist()
        self.twist_bebop = Twist()

        # Name of topic can change depending on name used in the code for
        # reading out the vive.
        rospy.Subscriber('twist1_pub_', Twist, self.get_vive_data)
        rospy.Subscriber('/bebop/odom', Odometry, self.get_bebop_data)

    def get_vive_data(self, data):
        """
        Updates pose data with vive measurements.
        """
        self.pose_vive = data

    def get_bebop_data(self, data):
        """
        Updates pose and twist data by using measurements on the bebop itself.
        """
        self.pose_bebop = data.pose.pose
        self.twist_bebop = data.twist.twist

if __name__ == '__main__':
    perception = Perception()