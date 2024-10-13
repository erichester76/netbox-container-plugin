# pylint: disable=C0103
"""Migration file"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration Class"""

    dependencies = [
        ('netbox_container_plugin', '0013_host_netbox_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='operation',
            field=models.CharField(default='create', max_length=32),
        ),
    ]
