# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20170611_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]