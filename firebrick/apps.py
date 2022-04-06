from django.apps import AppConfig
from firebrick.database import get_or_404


class FirebrickConfig(AppConfig):
    name = 'firebrick'