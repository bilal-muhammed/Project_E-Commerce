# Generated by Django 4.0.5 on 2022-09-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000235341C9630>', max_length=200),
        ),
    ]
