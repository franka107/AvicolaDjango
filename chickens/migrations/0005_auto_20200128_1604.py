# Generated by Django 3.0.2 on 2020-01-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chickens', '0004_auto_20200127_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
