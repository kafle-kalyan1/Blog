# Generated by Django 4.2.1 on 2023-05-27 08:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_remove_blog_descriptiom_blog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
