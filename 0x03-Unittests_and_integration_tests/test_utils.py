#!/usr/bin/env python3
"""
Unit Tests on Utils.py
"""
import unittest
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the `access_nested_map` function
    """
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
        Checking the Error raised is as expected
        """
        self.nested_dict = input1
        self.path = input2
        with self.assertRaises(KeyError) as aR:
            access_nested_map(input1, input2)


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
        Checking the get_json function's output
        """
        with patch('requests.get') as mock_req_get:
            mock_data = Mock(return_value=test_payload)
            mock_req_get.return_value.json = mock_data
            self.assertEqual(get_json(test_url), test_payload)
            mock_req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests the `memoize` function
    """
    def test_memoize(self):
        """
        Checking the output of the function
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method',\
                          return_value=lambda: 42) as mock_fn:
            # mock_fn.return_value = TestClass().a_method()
            my_class = TestClass()
            self.assertEqual(my_class.a_property(), 42)
            self.assertEqual(my_class.a_property(), 42)
            mock_fn.assert_called_once()



if __name__ == "__main__":
    unittest.main()
