# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20170517_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(blank=True, to='homepage.ShoesType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalog',
            name='sorting',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
