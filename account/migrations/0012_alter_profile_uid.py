# Generated by Django 4.0.5 on 2022-09-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000221E6BB9630>', max_length=200),
        ),
    ]