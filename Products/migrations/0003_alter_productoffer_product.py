# Generated by Django 4.0.5 on 2022-10-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realshop', '0003_products_cropping_alter_products_mimage'),
        ('Products', '0002_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoffer',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Offer', to='realshop.products'),
        ),
    ]
