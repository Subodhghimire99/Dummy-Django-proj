# Generated by Django 2.0.7 on 2019-01-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20190105_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failed',
            name='date',
        ),
    ]