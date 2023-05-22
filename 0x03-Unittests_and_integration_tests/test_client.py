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
    
    def test_public_repos_url(self):
        """
        Testing GithubOrgClient._public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            print(GithubOrgClient("google")._public_repos_url)
        self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Testing GithubOrgClient.public_repos.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 460600860,
                    "node_id": "R_kgDOG3Q2HA",
                    "name": ".allstar",
                    "full_name": "google/.allstar",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/.allstar",
                    "created_at": "2022-02-17T20:40:32Z",
                    "updated_at": "2023-04-03T17:58:33Z",
                    "has_issues": True,
                    "forks": 3,
                    "default_branch": "main"
                },
                {
                    "id": 170908616,
                    "node_id": "MDEwOlJlcG9zaXRvcnkxNzA5MDg2MTY=",
                    "name": ".github",
                    "full_name": "google/.github",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/.github",
                    "created_at": "2019-02-15T18:14:38Z",
                    "updated_at": "2023-04-15T18:17:55Z",
                    "has_issues": True,
                    "forks": 194,
                    "default_branch": "master"
                }
            ]
        }
        mock_get_json.return_value = test_payload['repos']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub_repos:
            mock_pub_repos.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    ".allstar",
                    ".github",
                ]
            )
            mock_pub_repos.assert_called_once()
        mock_get_json.assert_called_once()



            
if __name__ == "__main__":
    unittest.main()
