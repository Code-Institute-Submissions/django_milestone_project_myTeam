# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=16)),
                ('group_name', models.CharField(max_length=26)),
                ('password', models.CharField(max_length=160)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.DecimalField(decimal_places=0, max_digits=1)),
                ('admin', models.BooleanField()),
            ],
            options={
                'ordering': ('group_id',),
            },
        ),
    ]
