# Generated by Django 2.0.4 on 2018-06-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180522_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='rfid_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]