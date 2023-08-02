# Generated by Django 4.2.2 on 2023-06-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_freetrial_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardTitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Pricing_img')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
