# Generated by Django 5.0.2 on 2024-05-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompaniya_app', '0006_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('Director', 'director'), ('Marketing Manager', 'marketing_manager'), ('Selles Manager', 'selles_manager'), ('HR', 'HR')], max_length=60),
        ),
    ]