# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expeditions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='ship_rebuy',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='ship_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]