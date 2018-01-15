#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import LightSensorValues

class LightsensorTest(unittest.TestCase):
    def setUp(self):
        self.count = 0
        rospy.Subscriber('/lightsensors', LigthSensorValues, self.calback)
        self.values = LigthSensorValues

    def callback(self, data)
        self.count += 1
        self.values = data

    def check_values(self, lf, ls. rs. rf ):
        vs = self.values
        self.assertEqual(vs.left_forward, lf, "different value : left_forward" )
        self.assertEqual(vs.left_side, ls, "different value : left_side" )
        self.assertEqual(vs.right_side, rs, "different value : right_side" )
        self.assertEqual(vs.right_forward, rf, "different value : right_fowrard" )
        self.assertEqual(vs.sum_all, lf + ls + rs + rf, "different value : sum_all" )
        self.assertEqual(vs.sum_foard, lf + rf, "different value : sum_foward" )

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/lightsensors', nodes, "node does not exist")

    def test_get_value(self):
        rospy.set_param('lightsensors_freq', 10)
        time.sleep(2)
        with open("/dev/rtlightsensors0","w") as f:
            f.wtite("-1 0 123 4321")
   
        time.sleep(3)
        self.assertFalse(self.count == 0, "cannnot subscribe the topic")
        self.check_value(4321, 123, 0, -1)
    
    def test_change_paramater(self):
         rospy.set_param('loghtsensors_freq', 1 )
         time.sleep(2)
         c_prev = self.count
         time.sleep(3)
         
         self.assertTrue( self.count < c_prev + 4, "freq does not change")
         self.assertFalse( self.count == c_prev, "subscriber is stooped")

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_lightsensors')
    rostest.rosrun('pimouse_ros', 'travis_test_lightsensors', LightsensorTest)

