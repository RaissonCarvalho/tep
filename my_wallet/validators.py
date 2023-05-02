from django.core.exceptions import ValidationError
import re

def validate_stock_code(value):
    pattern = r'^[A-Z]{4}[0-9]{1,2}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'O código deve ter 5 ou 6 caracteres com os 4 primeiros sendo letras maiúsculas e os 5º e 6º caracteres sendo números.'
            )
    