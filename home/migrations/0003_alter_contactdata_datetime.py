# Generated by Django 4.2.1 on 2023-07-06 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contactdata_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 21, 52, 26, 627617)),
        ),
    ]
