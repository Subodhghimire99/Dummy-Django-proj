# Generated by Django 2.0.7 on 2019-01-05 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20190105_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='failed',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Division',
            field=models.CharField(choices=[('Dist', 'Distinction'), ('First', 'First Division'), ('Second', 'Second Division'), ('Third', 'Third Division'), ('Default', 'Not Selected')], default='Default', max_length=40),
        ),
    ]
