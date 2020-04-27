# Generated by Django 3.0.5 on 2020-04-27 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
