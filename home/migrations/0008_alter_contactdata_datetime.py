# Generated by Django 4.2.1 on 2023-05-27 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contactdata_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 27, 9, 23, 26, 859452)),
        ),
    ]
