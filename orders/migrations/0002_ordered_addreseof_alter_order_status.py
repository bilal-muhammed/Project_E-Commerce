# Generated by Django 4.0.5 on 2022-09-18 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered',
            name='addreseof',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.addrese'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order conformed', 'order Confirmed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('returned', 'returned'), ('return_accepted', 'return_accepted')], default='Order Confirmed', max_length=100),
        ),
    ]
