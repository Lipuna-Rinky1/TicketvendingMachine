# Generated by Django 3.2.13 on 2023-01-10 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0003_alter_token_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='token',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 12, 18, 50, 878845)),
        ),
    ]
