# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_oauth2codes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth2codes',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oauth2codes',
            name='user_id',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
