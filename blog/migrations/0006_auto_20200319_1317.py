# Generated by Django 3.0.3 on 2020-03-19 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200319_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='num_stars',
        ),
        migrations.RemoveField(
            model_name='album',
            name='release_date',
        ),
    ]
