# Generated by Django 4.0.1 on 2022-02-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
        ('users', '0003_alter_caertdetails_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminpanel.couponcode'),
        ),
    ]