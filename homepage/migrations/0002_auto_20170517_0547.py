# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(default=1, to='homepage.ShoesType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='sorting',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
