# Generated by Django 4.2.1 on 2023-06-16 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('conID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('dateTime', models.DateTimeField(default=datetime.datetime(2023, 6, 16, 6, 31, 32, 964377))),
            ],
        ),
    ]
