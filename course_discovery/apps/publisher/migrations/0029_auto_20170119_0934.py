# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-19 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0028_create_partner_manager_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Course Role'),
        ),
        migrations.AlterField(
            model_name='historicalcourseuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Course Role'),
        ),
        migrations.AlterField(
            model_name='historicalorganizationuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Organization Role'),
        ),
        migrations.AlterField(
            model_name='organizationuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('partner_coordinator', 'Partner Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Organization Role'),
        ),
    ]
