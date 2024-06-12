from __future__ import annotations
from typing import TYPE_CHECKING, Iterable

from mov_cli.config import Config
from mov_cli.http_client import HTTPClient

if TYPE_CHECKING:
    from typing import Optional, Dict

    from mov_cli import Config
    from mov_cli.http_client import HTTPClient

from pathlib import Path

from mov_cli import Single, Metadata, MetadataType

from mov_cli.scraper import Scraper
from mov_cli.utils import EpisodeSelector

__all__ = ("GoldyScraper",)

class GoldyScraper(Scraper):
    def __init__(self, config: Config, http_client: HTTPClient, options: Optional[Dict[str, str | bool]] = None) -> None:
        self.videos_path = Path(__file__).parent.joinpath("videos")

        super().__init__(config, http_client, options)

    def search(self, query: str, _: Optional[int] = None) -> Iterable[Metadata]:
        a_list = []

        for video in self.videos_path.iterdir():

            if video.name == ".gitkeep":
                continue

            if query.lower() in video.name.lower():

                a_list.append(
                    Metadata(
                        id = str(video.absolute()), 
                        title = video.name, 
                        type = MetadataType.SINGLE
                    )
                )

        return a_list

    def scrape(self, metadata: Metadata, _: EpisodeSelector) -> Single | None:

        return Single(
            url = metadata.id, 
            title = metadata.title, 
        )