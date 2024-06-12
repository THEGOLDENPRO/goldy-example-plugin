from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mov_cli.plugins import PluginHookData

from .scraper import *

plugin: PluginHookData = {
    "version": 1, # plugin hook version
    "package_name": "goldy-plugin", # pypi package name
    "scrapers": {
        "DEFAULT": GoldyScraper, 
    }
}

__version__ = "1.0.0"