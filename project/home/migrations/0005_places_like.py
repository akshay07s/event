# Generated by Django 3.1.7 on 2021-03-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_places_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
