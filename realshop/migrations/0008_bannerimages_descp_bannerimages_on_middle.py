# Generated by Django 4.0.5 on 2022-10-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realshop', '0007_category_offer_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimages',
            name='descp',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='bannerimages',
            name='on_middle',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
