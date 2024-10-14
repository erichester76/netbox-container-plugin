"""Netbox Plugin Configuration"""

from django.db.models.signals import post_migrate
from netbox.plugins import PluginConfig
from .utilities import create_webhook


class NetBoxDockerConfig(PluginConfig):
    """Plugin Config Class"""

    name = "netbox_container_plugin"
    verbose_name = "NetBox Container Plugin"
    description = "Manage Containers"
    version = "3.0.1"
    base_url = "docker"
    min_version = "4.1.0"
    author = "Vincent Simonin <vincent@saashup.com>, David Delassus <david.jose.delassus@gmail.com>"
    author_email = "vincent@saashup.com, david.jose.delassus@gmail.com"

    def ready(self):
        from . import signals  # pylint: disable=unused-import, import-outside-toplevel

        post_migrate.connect(create_webhook)

        super().ready()


# pylint: disable=C0103
config = NetBoxDockerConfig
