# Generated by Django 3.0.2 on 2020-01-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]