# Generated by Django 2.0.4 on 2018-05-21 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0002_auto_20180521_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='tent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='camping.Tent'),
        ),
    ]
