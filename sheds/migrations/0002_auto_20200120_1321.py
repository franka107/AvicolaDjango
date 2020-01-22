# Generated by Django 3.0.2 on 2020-01-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shedregister',
            name='chicken_quantity',
        ),
        migrations.RemoveField(
            model_name='shedregister',
            name='chicken_total',
        ),
        migrations.AlterField(
            model_name='shedregister',
            name='final_deposit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shedregister',
            name='food_consumption',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shedregister',
            name='food_deposit',
            field=models.IntegerField(default=0),
        ),
    ]