/*
/ BSD-3-Clause Lisence
/
/ Copyright © 2022, Shunsuke Umezawa. All right reserved.
*/


#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
