# Generated by Django 4.0.5 on 2022-10-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000162CDBB71C0>', max_length=200),
        ),
    ]