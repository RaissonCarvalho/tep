# Generated by Django 4.2 on 2023-04-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0005_alter_transaction_brokerage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='operation_type',
            field=models.CharField(choices=[('Compra', 'Compra'), ('Venda', 'Venda')], max_length=6),
        ),
    ]
