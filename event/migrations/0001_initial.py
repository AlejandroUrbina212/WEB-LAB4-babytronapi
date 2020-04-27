# Generated by Django 3.0.5 on 2020-04-27 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('baby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baby.Baby')),
            ],
        ),
    ]
