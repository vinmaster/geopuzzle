# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0019_auto_20170329_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('countries', models.ManyToManyField(to='maps.Country')),
            ],
        ),
    ]
