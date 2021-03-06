# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import resumes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=resumes.models.change_file_name)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('upload_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='지원자', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
