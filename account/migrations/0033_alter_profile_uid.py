# Generated by Django 4.0.5 on 2022-10-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000022BFD8E71C0>', max_length=200),
        ),
    ]
