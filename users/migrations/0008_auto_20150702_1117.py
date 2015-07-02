# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_lfuserprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lfuserprofile',
            old_name='lasName',
            new_name='lastName',
        ),
    ]
