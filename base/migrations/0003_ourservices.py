# Generated by Django 4.2.2 on 2023-06-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_whytochooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='services_img')),
                ('title', models.CharField(max_length=50)),
                ('descp', models.TextField(max_length=200)),
            ],
        ),
    ]
