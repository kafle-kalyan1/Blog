# Generated by Django 4.2.1 on 2023-07-25 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_contactdata_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 13, 34, 57, 871713)),
        ),
    ]
