# -*- coding: utf-8 -*-
"""Basic units test."""
import unittest
from github_api.api import GithubAPI


class TestAPI(unittest.TestCase):
    """Test througly the GithubAPI."""

    def test_fetch_releases(self):
        """
        Test that it can fetch the releases from Github.
        """
        api = GithubAPI()
        list_of_releases = api.fetch_releases("Darkness4/minitel-app")
        # print(list(map(lambda release: release.json, releases)))  # print all
        print(list_of_releases[0].html_url)


if __name__ == '__main__':
    unittest.main()
