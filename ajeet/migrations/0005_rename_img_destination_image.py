# Generated by Django 4.0 on 2023-01-17 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajeet', '0004_remove_destination_clas_remove_destination_contract_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='img',
            new_name='image',
        ),
    ]