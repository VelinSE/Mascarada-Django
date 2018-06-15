# Generated by Django 2.0.4 on 2018-06-15 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0004_auto_20180611_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='purchase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='others.Purchase'),
            preserve_default=False,
        ),
    ]
