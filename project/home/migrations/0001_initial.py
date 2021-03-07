# Generated by Django 3.1.7 on 2021-03-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/images')),
            ],
        ),
    ]
