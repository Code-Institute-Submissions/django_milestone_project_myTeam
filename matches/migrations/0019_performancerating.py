# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0002_auto_20190309_1352'),
        ('matches', '0018_matchdata_selected_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance_rating', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('performace_matchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_match_id', to='matches.MatchData')),
                ('performance_player_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_player_rated', to='profile_and_stats.UserProfileData')),
                ('performance_rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_rated_by', to='profile_and_stats.UserProfileData')),
            ],
        ),
    ]
