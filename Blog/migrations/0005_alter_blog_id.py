# Generated by Django 4.2.1 on 2023-05-27 05:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_rename_disc_blog_descriptiom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
