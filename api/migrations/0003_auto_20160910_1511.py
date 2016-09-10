# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160910_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='BelMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, default=9999)),
                ('topic', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='belstop',
            options={},
        ),
        migrations.RemoveField(
            model_name='belstop',
            name='created',
        ),
        migrations.AddField(
            model_name='belmeeting',
            name='belStop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BelStop'),
        ),
    ]
