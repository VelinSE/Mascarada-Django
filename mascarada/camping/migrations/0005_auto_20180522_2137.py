# Generated by Django 2.0.4 on 2018-05-22 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0004_auto_20180521_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camping',
            name='free_beds',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='spot',
            name='beds_taken',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
