# Generated by Django 4.2.7 on 2024-03-01 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sale_car_sale_client_sale_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]