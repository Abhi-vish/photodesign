# Generated by Django 4.2.2 on 2023-06-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
