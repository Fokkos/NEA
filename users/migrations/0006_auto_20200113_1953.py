# Generated by Django 3.0.2 on 2020-01-13 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200113_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
