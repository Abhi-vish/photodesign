# Generated by Django 4.2.2 on 2023-06-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_freetrial_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetrial',
            name='image',
            field=models.FileField(upload_to='Trial_image/'),
        ),
    ]
