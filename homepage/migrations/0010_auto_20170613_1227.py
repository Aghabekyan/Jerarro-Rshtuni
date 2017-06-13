# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20170518_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='massage',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
