from django.db import models
from .fields import PositiveFloatField
from .choices import OperationChoices
from accounts.models import Investor
from .validators import validate_stock_code


class Stock(models.Model):
    code = models.CharField(max_length=6, unique=True, blank=False, null=False, validators=[validate_stock_code])
    company_name = models.CharField(max_length=255, blank=False, null=False)
    cnpj = models.CharField(max_length=18, blank=False, null=False)

    def __str__(self):
        return f"{self.code} - {self.company_name} ({self.cnpj})"
    

class Transaction(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=6, choices=OperationChoices.choices)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    unit_price = PositiveFloatField()
    brokerage = PositiveFloatField()
    date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f"{self.investor.name} - {self.stock.code} ({self.operation_type}) - {self.quantity} - {self.unit_price} - {self.date}"
    

    def get_total_trading_amount(self):
        if self.operation_type == 'Compra':
            total_value = (self.quantity * self.unit_price) + (self.brokerage+0.003)
            return total_value
        if self.operation_type == 'Venda':
            total_value = (self.quantity * self.unit_price) - (self.brokerage+0.003)
            return round(abs(total_value), 2)