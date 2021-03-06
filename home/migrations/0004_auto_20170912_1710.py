# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170829_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_cellPhone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_homePhone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_orgtype',
            field=models.CharField(choices=[('household', 'Household'), ('organization', 'Organization')], default='household', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_zip',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
