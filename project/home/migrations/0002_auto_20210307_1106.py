# Generated by Django 3.1.7 on 2021-03-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='image',
            field=models.ImageField(upload_to='event_images'),
        ),
    ]