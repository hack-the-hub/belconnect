# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='belmeeting',
            name='category',
            field=models.IntegerField(choices=[(12, 'Other'), (1, 'Culture'), (3, 'Sports'), (4, 'History'), (5, 'Music'), (6, 'Social'), (7, 'Politics'), (8, 'Tech'), (9, 'Travel'), (10, 'Hobbies'), (11, 'Family'), (12, 'Other')], default=12),
        ),
    ]
