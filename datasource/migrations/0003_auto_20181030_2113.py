# Generated by Django 2.1.2 on 2018-10-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0002_auto_20181030_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='original_zip',
            field=models.CharField(max_length=5),
        ),
    ]
