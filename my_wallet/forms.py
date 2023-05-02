from django import forms
from .models import Stock, Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = (
            'investor',
          )

        widgets = {
            'stock': forms.Select(attrs={'class': 'form-select'}),
            'operation_type': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'name': 'Preço unitário'}),
            'brokerage': forms.NumberInput(attrs={'class': 'form-control'}),     
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.all()


class UpdateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = (
            'stock',
            'investor',
          )

        widgets = {
            'operation_type': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'name': 'Preço unitário'}),
            'brokerage': forms.NumberInput(attrs={'class': 'form-control'}),     
        }