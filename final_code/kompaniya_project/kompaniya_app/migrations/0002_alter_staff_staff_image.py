# Generated by Django 5.0.2 on 2024-05-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompaniya_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_image',
            field=models.ImageField(blank=True, null=True, upload_to='staffs_images/'),
        ),
    ]