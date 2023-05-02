# Generated by Django 4.2 on 2023-04-26 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='brokerage',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, 'Valor não pode ser zero ou negativo')]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]