# Generated by Django 4.1 on 2022-09-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_empleos_informacion_personas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='personas',
            name='fecha_nacimiento',
            field=models.EmailField(max_length=254),
        ),
    ]
