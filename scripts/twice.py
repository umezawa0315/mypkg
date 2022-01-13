#!/usr/bin/env python3

# BSD-3-Clause Lisence

# Copyright © 2022, Shunsuke Umezawa. All rights reserved. 



import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32,cb)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        if n % 2 == 0 and n != 0:

            if n % 3 == 0:
                print('[%d]は\n2の倍数' % n)

                if n % 5 == 0:
                    print('3の倍数\n5の倍数です。\n')

                else:
                    print('3の倍数です。\n')

            elif n % 5 == 0:
                print('[%d]は\n2の倍数\n5の倍数です。\n' % n)

            else:
                print('[%d]は\n2の倍数です。\n' % n)

        if n % 2 != 0 and n % 3 == 0:

            if n % 5 == 0: 
                print('[%d]は\n3の倍数\n5の倍数です。\n' % n)

            else:
                print('[%d]は\n3の倍数です。\n' % n)

        if n % 2 != 0 and n % 3 != 0:

            if n % 5 == 0:
                print('[%d]は\n5の倍数です。\n' % n)

            else:
                print('[%d]は\n2.3.5の倍数ではありません。\n' % n)

        if n == 0:
            print('[%d]は\n2.3.5の倍数ではありません。\n' % n)

        pub.publish(n)
        rate.sleep()
