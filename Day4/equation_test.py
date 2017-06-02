import unittest
from equation import *


class Tests(unittest.TestCase):
    def test_type_error(self):
        self.assertIsNone(resolution(1, "sdf", 2.0))

    def test_is_no_zero_and_delta_little_than_zero(self):
        self.assertListEqual([0,{}] , resolution(3, 1, 1))
    def test_is_no_zero_and_delta_equals_zero(self):
        self.assertListEqual([1, {-1}] , resolution(1, 2, 1))
    def test_is_no_zero_and_delta_great_than_zero(self):
        self.assertListEqual([2,{-1,-0.3333333333333333}] , resolution(3, 4, 1))

    def test_is_all_equal_0(self):
        self.assertIsNone(resolution(0, 0, 0))
    def test_is_not_all_0_and_bc_notequals_0(self):
        self.assertListEqual([1, {-1}] , resolution(0, 1, 1))
    def test_is_not_all_0_and_ab_notequals_0(self):
        self.assertListEqual([2, {0,-1}] , resolution(1, 1, 0))
    def test_is_not_all_0_and_a_equals_0(self):
        self.assertListEqual([0,{}] , resolution(0, 1, 0))
    def test_is_not_all_0_and_ac_little_than_0(self):
        self.assertListEqual([0,{}] , resolution(-1, 0, 1))
    def test_is_not_all_0_and_b_equals_0_sqrt_equals_0(self):
        self.assertListEqual([1,{0}] , resolution(-1, 0, 0))
    def test_is_not_all_0_and_b_equals_0_sqrt_notequals_0(self):
        self.assertListEqual([2,{2.0,-2.0}] , resolution(1, 0, 4))

unittest.main()
