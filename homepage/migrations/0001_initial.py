# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(default=b'', upload_to=homepage.models.get_file_path_img)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
    ]
