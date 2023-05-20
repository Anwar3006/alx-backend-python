#!/usr/bin/env python3
"""
Unit Tests on Utils.py
"""
import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch, Mock


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
            utils.access_nested_map(
                self.nested_dict,
                self.path),
            output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, input1, input2):
        """
        Checking the Error raised is as expected
        """
        self.nested_dict = input1
        self.path = input2
        with self.assertRaises(KeyError) as aR:
            utils.access_nested_map(input1, input2)


class TestGetJson(unittest.TestCase):
    """
    Tests the `get_json` function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test the get_json function's output
        """
        with patch('requests.get') as mock_req_get:
            mock_data = Mock(return_value=test_payload)
            mock_req_get.return_value.json = mock_data
            self.assertEqual(utils.get_json(test_url), test_payload)
            mock_req_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
