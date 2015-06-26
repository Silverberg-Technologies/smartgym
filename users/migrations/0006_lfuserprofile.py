# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150528_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='LFUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('age', models.IntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('lasName', models.CharField(max_length=255)),
                ('nickName', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('height', models.FloatField()),
                ('heightUnit', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('weightUnit', models.CharField(max_length=255)),
                ('preferredUnit', models.CharField(max_length=255)),
                ('createdOn', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
