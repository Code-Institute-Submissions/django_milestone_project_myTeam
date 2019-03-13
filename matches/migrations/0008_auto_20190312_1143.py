# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20190311_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytable',
            name='matchID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='matches.MatchData'),
        ),
        migrations.AlterField(
            model_name='availabilitytable',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='profile_and_stats.UserProfileData'),
        ),
        migrations.AlterField(
            model_name='matchdata',
            name='associated_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_group', to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='matchdata',
            name='players',
            field=models.ManyToManyField(related_name='linked_players', to='profile_and_stats.UserProfileData'),
        ),
    ]
