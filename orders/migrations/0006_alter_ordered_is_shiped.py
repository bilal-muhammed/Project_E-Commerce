# Generated by Django 4.0.5 on 2022-10-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_ordered_is_shiped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='is_shiped',
            field=models.BooleanField(default=False),
        ),
    ]
