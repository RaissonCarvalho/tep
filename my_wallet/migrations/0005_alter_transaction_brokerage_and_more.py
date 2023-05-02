# Generated by Django 4.2 on 2023-04-26 20:41

from django.db import migrations
import my_wallet.fields


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0004_alter_transaction_brokerage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='brokerage',
            field=my_wallet.fields.PositiveFloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='unit_price',
            field=my_wallet.fields.PositiveFloatField(),
        ),
    ]