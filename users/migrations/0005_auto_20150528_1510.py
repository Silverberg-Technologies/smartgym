# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150528_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oauth2codes',
            old_name='user_id',
            new_name='user',
        ),
    ]
