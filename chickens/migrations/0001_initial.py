# Generated by Django 3.0.2 on 2020-01-18 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sheds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField()),
                ('week_age', models.IntegerField()),
                ('entry_date', models.DateField()),
                ('chicken_type', models.CharField(choices=[('HSX', 'HYSEX'), ('HSN', 'H.NEGRA'), ('HYN', 'HYN'), ('LMN', 'LOHMAN'), ('NVG', 'NOVOGEN')], max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shed', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sheds.Shed')),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
            },
        ),
    ]
