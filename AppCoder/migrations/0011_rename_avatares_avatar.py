# Generated by Django 4.1 on 2022-10-19 04:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0010_rename_avatar_avatares'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatares',
            new_name='Avatar',
        ),
    ]
