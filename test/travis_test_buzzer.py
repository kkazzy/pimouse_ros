#!/usr/bin/env python
#encoding: utf8
import rospy, unittest, rostest, actionlib
import rosnode
import time
from std_msgs.msg import UInt16
from pimouse_ros.msg import MusicAction, MusicResult, MUsicFeedback, MusicGoal

class BuzzerTest(unittest.TestCase):
    def setUp(self):
        self.client = actionlib.SimpleActionClient("music", MusicAction)
        self.device_values = []
        # デバイスファイルに書き出された値を採取しておくリスト
 
    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/buzzer', nodes, "node does not exist")

    def test_put_travis(self):
        pub = rospy.Publisher('/buzzer', UInt16)
        for i in range(10):
            pub.publish(1234)
            time.sleep(0.1)
        
        with open("/dev/rtbuzzer0", "r") as f:
            data = f.readline()
            self.assertEqual( data, "1234\n", "value does not written to rtbuzzer0") 

    def test_music(self):
        goal = MusicGoal()
        goal.freqs = [100,200,300,0]
        goal.durations = [2,2,2,2]

        self.client.wait_for_server()
        self.client.send_goal( goal, feedback_cb=self.feedback_cb)
        self.client.wait_for_result()


    def feedback_cb(self):
        with open("/dev/rtbuzzer0", "r") as f:
            data = f.readline()
            self.device_values.append(int(data.rstrip()))


if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_buzzer')
    rostest.rosrun('pimouse_ros', 'travis_test_buzzer', BuzzerTest)

