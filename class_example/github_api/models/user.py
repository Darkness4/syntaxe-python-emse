# -*- coding: utf-8 -*-
"""Github API partial User Model.

This module creates a inspired Github User model so that it can be easily used
from a package.

"""


class GithubUser:
    """Github User model."""

    def __init__(
            self,
            url: str = "",
            login: str = "",
            html_url: str = "",
            avatar_url: str = "",
            self_id: int = -1,
    ):
        self.url = url
        self.login = login
        self.html_url = html_url
        self.avatar_url = avatar_url
        self.self_id = self_id

    @classmethod
    def from_json(
            cls,
            json: dict,
    ):  # Constructor with a name
        """Import from a dict."""

        return cls(
            login=json['login'],
            self_id=json['id'],
            html_url=json['html_url'],
            url=json['url'],
            avatar_url=json['avatar_url'],
        )

    @property
    def json(self) -> dict:
        """Export to a dict."""
        return {
            "login": self.login,
            "id": self.self_id,
            "html_url": self.html_url,
            "url": self.url,
            "avatar_url": self.avatar_url,
        }
