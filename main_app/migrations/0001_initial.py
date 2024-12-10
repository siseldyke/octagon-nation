# Generated by Django 5.1.4 on 2024-12-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weight_class', models.DecimalField(decimal_places=1, max_digits=5)),
                ('is_title_fight', models.BooleanField(default=False)),
                ('attendees', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]