# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupsession',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date_time', models.DateTimeField(verbose_name='date and time of session')),
                ('location', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('available_slots', models.IntegerField()),
                ('instructor', models.ForeignKey(related_name='group_instructor', to=settings.AUTH_USER_MODEL)),
                ('users_attending', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LFUserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('nickName', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('height', models.FloatField()),
                ('heightUnit', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('weightUnit', models.CharField(max_length=255)),
                ('preferredUnit', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Oauth2Codes',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=128)),
                ('refresh_token', models.CharField(max_length=128)),
                ('expire_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SmartGymUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_instructor', models.BooleanField()),
                ('is_moderator', models.BooleanField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
