# Generated by Django 4.0 on 2023-01-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajeet', '0003_alter_destination_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='clas',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='email',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='more',
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
