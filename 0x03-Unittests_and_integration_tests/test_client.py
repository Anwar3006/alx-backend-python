#!/usr/bin/env python3
"""
Testing the clients script
"""
import unittest
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Checking the Githib org client class
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org, response, mock_get_json):
        """
        Testing the `org` method for correct return
        """
        mock_get_json.return_value = MagicMock(return_value=response)
        org_client_obj = GithubOrgClient(org)
        self.assertEqual(org_client_obj.org(), response)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

if __name__ == "__main__":
    unittest.main()
