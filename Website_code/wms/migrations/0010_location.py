# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0009_auto_20171012_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantID', models.IntegerField(unique=True)),
                ('latitude', models.FloatField(default=13.549549)),
                ('longitude', models.FloatField(default=79.99999)),
            ],
        ),
    ]
