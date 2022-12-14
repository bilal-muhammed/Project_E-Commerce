# Generated by Django 4.0.5 on 2022-10-02 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0007_alter_order_status_alter_ordered_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed_by', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Razorpay', 'Razorpay'), ('Paypal', 'Paypal')], default='Pending', max_length=100)),
                ('amount_is', models.CharField(max_length=200)),
                ('Order_id', models.CharField(max_length=200)),
                ('date_at', models.DateTimeField(auto_now_add=True)),
                ('orderof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ordered')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
