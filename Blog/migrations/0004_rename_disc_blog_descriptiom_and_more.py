# Generated by Django 4.2.1 on 2023-05-27 04:54

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blog_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='disc',
            new_name='descriptiom',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='bTitle',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='bId',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='num',
        ),
        migrations.AddField(
            model_name='blog',
            name='coverImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Static/BLogs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
