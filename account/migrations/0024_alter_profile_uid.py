# Generated by Django 4.0.5 on 2022-10-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001C1AC269C60>', max_length=200),
        ),
    ]