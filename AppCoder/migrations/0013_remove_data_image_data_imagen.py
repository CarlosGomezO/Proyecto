# Generated by Django 4.1 on 2022-10-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_imagenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='image',
        ),
        migrations.AddField(
            model_name='data',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen'),
        ),
    ]
