# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oauth2Codes',
            fields=[
                ('user_id', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('access_token', models.CharField(max_length=128)),
                ('refresh_token', models.CharField(max_length=128)),
                ('expires_in', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='groupsession',
            name='coach',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='groupsession',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
