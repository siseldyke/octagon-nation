# Generated by Django 5.1.4 on 2024-12-10 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_title_fight',
        ),
        migrations.RemoveField(
            model_name='event',
            name='weight_class',
        ),
    ]
