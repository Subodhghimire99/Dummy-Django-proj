# Generated by Django 2.0.7 on 2019-01-17 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_detail_desctiption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='Desctiption',
            new_name='Description',
        ),
    ]