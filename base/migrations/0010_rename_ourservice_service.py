# Generated by Django 4.2.2 on 2023-06-28 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_ourservice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurService',
            new_name='Service',
        ),
    ]
