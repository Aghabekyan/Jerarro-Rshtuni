# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='answer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
