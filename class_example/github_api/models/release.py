# -*- coding: utf-8 -*-
"""Github API partial Release Model.

This module creates a partial replication of a `Github Release` so that it can
be easily used from a package.

.. Github Release:
    https://developer.github.com/v3/repos/releases/#get-a-single-release

"""
from datetime import datetime
from typing import List

from .user import GithubUser
from .asset import GithubAsset


class GithubRelease:
    """Github Release model."""

    def __init__(
            self,
            url: str = "",
            tag_name: str = "",
            name: str = "",
            html_url: str = "",
            author: GithubUser = GithubUser(),
            self_id: int = -1,
            created_at: datetime = datetime.now(),
            published_at: datetime = datetime.now(),
            assets: List[GithubAsset] = [],
            body: str = "",
    ):
        """Default constructor"""
        self.url = url
        self.tag_name = tag_name
        self.name = name
        self.html_url = html_url
        self.author = author
        self.self_id = self_id
        self.created_at = created_at
        self.published_at = published_at
        self.assets = assets
        self.body = body

    @classmethod
    def from_json(
            cls,
            json: dict,
    ):  # Constructor with a name
        """Import from a dict."""

        return cls(
            url=json["url"],
            tag_name=json["tag_name"],
            name=json["name"],
            html_url=json["html_url"],
            self_id=json["id"],
            author=GithubUser.from_json(json["author"]),
            created_at=datetime.fromisoformat(
                str(json["created_at"]).replace("Z", "+00:00")),
            published_at=datetime.fromisoformat(
                str(json["published_at"]).replace("Z", "+00:00")),
            assets=list(map(GithubAsset.from_json, json["assets"])),
            body=json["body"],
        )

    @property
    def json(self) -> dict:
        """Return a dict."""
        return {
            "url": self.url,
            "tag_name": self.tag_name,
            "name": self.name,
            "html_url": self.html_url,
            "id": self.self_id,
            "author": self.author.json,
            "created_at": self.created_at.isoformat(),
            "published_at": self.published_at.isoformat(),
            "assets": list(map(lambda asset: asset.json, self.assets)),
            "body": self.body,
        }
