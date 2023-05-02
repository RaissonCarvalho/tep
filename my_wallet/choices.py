from django.db.models import TextChoices

class OperationChoices(TextChoices):
    COMPRA = 'Compra', 'Compra'
    VENDA = 'Venda', 'Venda'