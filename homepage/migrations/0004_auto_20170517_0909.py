# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20170517_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='img',
            field=models.ImageField(default=b'', null=True, upload_to=homepage.models.get_file_path_img, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catalog',
            name='sorting',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
