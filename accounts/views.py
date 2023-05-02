from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import InvestorForm
from .models import Investor
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class InvestorFormView(FormView):
    template_name = 'signup.html'
    form_class = InvestorForm

    success_url = reverse_lazy('login')

    def form_valid(self, form: form_class) -> HttpResponse:
        user = User.objects.create_user(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],

        )

        Investor.objects.create(
            name=form.cleaned_data['name'],
            risk_profile=form.cleaned_data['risk_profile'],
            user=user,
        )

        return super().form_invalid(form)
  