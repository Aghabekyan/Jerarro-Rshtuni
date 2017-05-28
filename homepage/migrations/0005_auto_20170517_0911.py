# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20170517_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='img',
            field=models.ImageField(default=b'', max_length=255, null=True, upload_to=homepage.models.get_file_path_img, blank=True),
            preserve_default=True,
        ),
    ]
