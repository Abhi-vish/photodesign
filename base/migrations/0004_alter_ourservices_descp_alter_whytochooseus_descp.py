# Generated by Django 4.2.2 on 2023-06-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_ourservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservices',
            name='descp',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='whytochooseus',
            name='descp',
            field=models.TextField(),
        ),
    ]