# Generated by Django 3.0 on 2019-12-18 14:54

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20191210_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='teste'),
            preserve_default=False,
        ),
    ]
