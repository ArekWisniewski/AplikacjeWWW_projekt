# Generated by Django 4.1.4 on 2022-12-18 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_customer_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='products',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('data', models.DateField(default=datetime.datetime(2022, 12, 18, 18, 25, 26, 375993))),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
            ],
        ),
    ]
