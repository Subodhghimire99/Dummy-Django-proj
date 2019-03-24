# Generated by Django 2.0.7 on 2019-01-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Rollno', models.CharField(max_length=7)),
                ('Percentage', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Country', models.CharField(max_length=40)),
            ],
        ),
    ]