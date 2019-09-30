# -*- coding: utf-8 -*-
"""Github API package.

Used in OOP programming, the response of the github API is separated in
multiple models.

Right now, it contains:

- Asset
- Release
- User

The current state of the package makes that it can only `List releases for a
repository`.

.. List releases for a repository
    https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository

"""
from typing import List
import json
import requests

from github_api.models.release import GithubRelease


class GithubAPI:
    """Github API handler."""

    def fetch_releases(self, repo: str) -> List[GithubRelease]:
        """Fetch the releases from repo.

        Exemple:
            To use::

                >>> list_of_releases = fetch_releases("my-user/my-repo")
                >>> print(list_of_releases[0].html_url)
                https://github.com/my-user/my-repop/releases/tag/my-tag
        """
        response = requests.get(
            "https://api.github.com/repos/{}/releases".format(repo))
        if response.status_code == 200:
            return list(
                map(GithubRelease.from_json,
                    json.loads(response.content.decode('utf-8'))))
        else:
            return None
