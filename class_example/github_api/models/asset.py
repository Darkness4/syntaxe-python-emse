# -*- coding: utf-8 -*-
"""Github API partial Asset Model.

This module creates a partial replication of a `Github Asset` so that it can be
easily used from a package.

.. Github Asset:
    https://developer.github.com/v3/repos/releases/#get-a-single-release-asset

"""
from datetime import datetime
from .user import GithubUser


class GithubAsset:
    """Github Asset model."""

    def __init__(
            self,
            url: str = "",
            name: str = "",
            download_count: int = -1,
            browser_download_url: str = "",
            uploader: GithubUser = GithubUser(),
            self_id: int = -1,
            size: int = -1,
            created_at: datetime = datetime.now(),
            updated_at: datetime = datetime.now(),
    ):
        self.url = url
        self.name = name
        self.download_count = download_count
        self.browser_download_url = browser_download_url
        self.uploader = uploader
        self.self_id = self_id
        self.size = size
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_json(
            cls,
            json: dict,
    ):  # Constructor with a name
        """Import from a dict."""

        return cls(
            url=json["url"],
            name=json["name"],
            browser_download_url=json["browser_download_url"],
            self_id=json["id"],
            size=json["size"],
            download_count=json["download_count"],
            uploader=GithubUser.from_json(json["uploader"]),
            created_at=datetime.fromisoformat(
                str(json["created_at"]).replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(
                str(json["updated_at"]).replace("Z", "+00:00")),
        )

    @property
    def json(self) -> dict:
        """Export to a dict."""
        return {
            "url": self.url,
            "name": self.name,
            "browser_download_url": self.browser_download_url,
            "id": self.self_id,
            "size": self.size,
            "download_count": self.download_count,
            "uploader": self.uploader.json,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
