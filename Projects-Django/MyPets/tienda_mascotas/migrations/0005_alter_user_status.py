# Generated by Django 3.2.7 on 2021-10-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0004_auto_20211010_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(),
        ),
    ]
