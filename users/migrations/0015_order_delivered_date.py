# Generated by Django 4.0.1 on 2022-02-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]