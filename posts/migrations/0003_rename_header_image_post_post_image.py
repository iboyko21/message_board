# Generated by Django 3.2.7 on 2021-09-12 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='post_image',
        ),
    ]
