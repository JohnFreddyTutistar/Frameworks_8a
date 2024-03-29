# Generated by Django 3.2.7 on 2021-10-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('id_country', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='identification_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True)),
                ('id_user', models.IntegerField()),
                ('id_type', models.IntegerField()),
                ('id_race', models.IntegerField()),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('ip', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('delete_at', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='delete_at',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]
