# Generated by Django 3.1.5 on 2021-02-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upravlenie', '0005_auto_20210201_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumingotoplenie',
            name='otklonenie',
            field=models.FloatField(),
        ),
    ]