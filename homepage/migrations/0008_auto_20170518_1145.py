# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_contacts_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='comment',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='massage',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
    ]
