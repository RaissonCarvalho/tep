from typing import Any, Dict
from django import forms
from .models import Investor
from .choices import RiskProfileChoices

class InvestorForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Digite sua senha', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
      model = Investor
      fields = ['name', 'risk_profile']
      labels = {
        'name': 'Nome completo',
        'risk_profile': 'Perfil de Risco',
        }
      widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'risk_profile': forms.Select(choices=RiskProfileChoices.choices, attrs={'class': 'form-control'})
      }
      