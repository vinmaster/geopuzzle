# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/puzzles'),
        ),
    ]
