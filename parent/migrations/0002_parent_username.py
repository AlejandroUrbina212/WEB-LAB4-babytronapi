# Generated by Django 3.0.5 on 2020-04-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='username',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
