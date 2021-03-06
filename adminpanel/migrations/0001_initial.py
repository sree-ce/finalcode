# Generated by Django 4.0.1 on 2022-02-09 07:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('discount', models.FloatField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10)),
                ('valid_from', models.DateField(blank=True)),
                ('valid_to', models.DateField(blank=True)),
                ('discount', models.FloatField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)])),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True, max_length=120)),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Red', 'Red'), ('Pink', 'Pink'), ('Green', 'Green'), ('Purple', 'Purple'), ('Yellow', 'Yellow'), ('Violet', 'Violet'), ('White', 'White'), ('Orange', 'Orange'), ('Blue', 'Blue')], max_length=200)),
                ('stock', models.IntegerField(blank=True, default=1, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='medias', verbose_name='')),
                ('images2', models.ImageField(blank=True, null=True, upload_to='medias', verbose_name='')),
                ('images3', models.ImageField(blank=True, null=True, upload_to='medias', verbose_name='')),
                ('total_price', models.FloatField(blank=True, max_length=20, null=True)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.category')),
            ],
        ),
        migrations.CreateModel(
            name='sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='productimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='medias', verbose_name='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.sizes'),
        ),
    ]
