# Generated by Django 4.2.2 on 2023-06-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_ourservices_descp_alter_whytochooseus_descp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howwework',
            name='about',
            field=models.TextField(),
        ),
    ]