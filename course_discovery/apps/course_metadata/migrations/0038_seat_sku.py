# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-23 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0037_migrate_courses_with_canonical'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='sku',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
