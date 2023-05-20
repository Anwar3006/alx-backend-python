#!/usr/bin/env python3
"""
Unit Tests on Utils.py
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
import sys


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        (1, {"a": 1}, ("a",)),
        (2, {"a": {"b": 2}}, ("a", "b")),
        (2, {"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, output, input1, input2):
        """
        Checking the output of the function using parameterized module
        to check multiple inputs
        _______
        Expected output:
        OK
        Fail
        OK
        """
        self.nested_dict = input1
        self.path = input2
        self.assertEqual(
            access_nested_map(
                self.nested_dict,
                self.path),
            output)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, input1, input2):
        """
        Checking the 
        """
        self.nested_dict = input1
        self.path = input2
        with self.assertRaises(KeyError) as aR:
            access_nested_map(input1, input2)

if __name__ == "__main__":
    unittest.main()
