# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-22 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_info_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='ans1score',
            field=models.IntegerField(default=0, verbose_name='Ans 1 score'),
        ),
        migrations.AddField(
            model_name='info',
            name='ans2score',
            field=models.IntegerField(default=0, verbose_name='Ans 2 score'),
        ),
        migrations.AddField(
            model_name='info',
            name='ans3score',
            field=models.IntegerField(default=0, verbose_name='Ans 3 score'),
        ),
        migrations.AddField(
            model_name='info',
            name='ans4score',
            field=models.IntegerField(default=0, verbose_name='Ans 4 score'),
        ),
        migrations.AddField(
            model_name='info',
            name='ans5score',
            field=models.IntegerField(default=0, verbose_name='Ans 5 score'),
        ),
    ]
