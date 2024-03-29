# Generated by Django 4.1.3 on 2023-03-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animemovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('img', models.ImageField(upload_to='pics')),
                ('discription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('img', models.ImageField(upload_to='pics')),
                ('discription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('number', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]
