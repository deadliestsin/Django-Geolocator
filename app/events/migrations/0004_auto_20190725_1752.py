# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-25 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190725_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='events.EventType'),
        ),
    ]
