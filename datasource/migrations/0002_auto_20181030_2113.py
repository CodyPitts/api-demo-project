# Generated by Django 2.1.2 on 2018-10-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='original_zip',
            field=models.CharField(max_length=6),
        ),
    ]
