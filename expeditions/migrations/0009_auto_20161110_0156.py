# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expeditions', '0008_registration_retracted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
