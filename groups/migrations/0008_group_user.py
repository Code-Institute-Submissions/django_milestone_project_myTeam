# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-01 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0002_auto_20190228_1350'),
        ('groups', '0007_groupmember_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(to='profile_and_stats.UserProfileData'),
        ),
    ]
