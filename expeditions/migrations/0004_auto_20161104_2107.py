# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expeditions', '0003_auto_20161103_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='teaser_image',
            field=models.URLField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
