# Generated by Django 4.1 on 2022-10-19 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0009_alter_avatar_options_rename_image_avatar_imagen_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatar',
            new_name='Avatares',
        ),
    ]
