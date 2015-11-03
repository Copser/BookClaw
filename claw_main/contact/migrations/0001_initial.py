# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=250)),
                ('topic', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
