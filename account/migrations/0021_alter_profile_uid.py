# Generated by Django 4.0.5 on 2022-10-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001C4BB039630>', max_length=200),
        ),
    ]
