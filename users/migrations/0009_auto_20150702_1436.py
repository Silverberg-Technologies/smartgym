# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150702_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oauth2codes',
            name='expires_in',
        ),
        migrations.AddField(
            model_name='oauth2codes',
            name='expire_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
