# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 18:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='id',
        ),
        migrations.AlterField(
            model_name='resume',
            name='upload_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='지원자', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]