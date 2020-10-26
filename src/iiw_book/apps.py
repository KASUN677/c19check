import os
import logging

from django.apps import AppConfig
from django.core.cache import cache
from django.db.utils import ProgrammingError

import requests

logger = logging.getLogger(__name__)

AGENT_URL = os.environ.get("AGENT_URL")


class IIWBookConfig(AppConfig):
    name = "iiw_book"

    def ready(self):
        # Hack to let the manage command to create the cache table through...
        try:
            cache.get("")
        except ProgrammingError:
            return


