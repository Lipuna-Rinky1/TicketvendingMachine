# Generated by Django 3.2.13 on 2023-01-10 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0002_auto_20230109_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 11, 39, 27, 760134)),
        ),
    ]
