# Generated by Django 4.2.1 on 2023-07-25 18:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blog_options_alter_blog_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='coverImage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
