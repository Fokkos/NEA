# Generated by Django 3.0.2 on 2020-01-27 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20200120_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=280)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='main.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
