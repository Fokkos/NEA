# Generated by Django 3.0.2 on 2020-01-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200116_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='media/pfps/default.png', upload_to='media/pfps'),
        ),
    ]
