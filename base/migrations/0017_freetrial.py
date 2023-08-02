# Generated by Django 4.2.2 on 2023-06-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_service_desc6'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeTrial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Trial_image')),
                ('comment', models.TextField()),
            ],
        ),
    ]
