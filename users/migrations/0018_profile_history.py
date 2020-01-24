# Generated by Django 3.0.2 on 2020-01-23 12:21

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_profile_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='history',
            field=models.CharField(default='', max_length=250, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
