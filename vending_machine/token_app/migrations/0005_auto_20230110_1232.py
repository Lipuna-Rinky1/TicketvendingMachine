# Generated by Django 3.2.13 on 2023-01-10 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0004_auto_20230110_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 12, 32, 27, 630384)),
        ),
        migrations.AlterField(
            model_name='token',
            name='patient_name',
            field=models.CharField(max_length=50),
        ),
    ]
