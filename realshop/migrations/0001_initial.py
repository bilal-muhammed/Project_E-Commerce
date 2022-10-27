# Generated by Django 4.0.5 on 2022-09-17 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Images', models.ImageField(upload_to='media/banner/')),
                ('is_active', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categories', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('Descp', models.TextField()),
                ('price', models.FloatField(null=True)),
                ('Mimage', models.FileField(default=True, upload_to='media/Product_Mimage')),
                ('available_is', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realshop.category')),
            ],
        ),
        migrations.CreateModel(
            name='productImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='media/Product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realshop.products')),
            ],
        ),
    ]