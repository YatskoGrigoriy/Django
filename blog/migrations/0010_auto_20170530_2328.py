# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-30 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170530_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog_images/', verbose_name='Ваше фото'),
        ),
    ]
