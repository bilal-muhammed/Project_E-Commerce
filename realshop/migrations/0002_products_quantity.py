# Generated by Django 4.0.5 on 2022-09-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]