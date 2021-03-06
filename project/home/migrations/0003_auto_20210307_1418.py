# Generated by Django 3.1.7 on 2021-03-07 08:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210307_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='places',
            name='like_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
