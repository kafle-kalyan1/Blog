# Generated by Django 4.2.1 on 2023-07-19 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_contactdata_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 23, 11, 32, 287835)),
        ),
    ]
