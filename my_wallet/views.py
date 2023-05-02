from accounts.models import Investor
from .forms import TransactionForm, UpdateTransactionForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView, DetailView,DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from my_wallet.models import Stock, Transaction



class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
      context = super(DashboardTemplateView, self).get_context_data(**kwargs)
      context['investor'] = get_investor(request=self.request)
      context['stocks'] = Stock.objects.all()

      return context
    
class TransactionsTemplateView(TemplateView):
    template_name = 'transactions.html'

    def get_context_data(self, **kwargs):
      context = super(TransactionsTemplateView, self).get_context_data(**kwargs)
      context['investor'] = get_investor(request=self.request)

      context['transactions'] = Transaction.objects.filter(investor=context['investor']).order_by('date')

      if 'code' in self.request.GET:
        code = self.request.GET['code']
        context['transactions'] = context['transactions'].filter(stock__code=code)

      return context
    

class TransactionDetailView(DetailView):
  template_name = 'transaction-details.html'

  model = Transaction
  context_object_name = 'transaction'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    return context

class TransactionUpdateView(SuccessMessageMixin, UpdateView):
  model = Transaction
  template_name = 'transaction-form.html'

  form_class = UpdateTransactionForm
  
  success_message = "Transação atualizada com sucesso!"
  success_url = reverse_lazy('dashboard')


class TransactionDeleteView(SuccessMessageMixin, DeleteView):
   model = Transaction
   success_url = reverse_lazy('transactions')
   success_message = "Transação deletada com sucesso!"
  

class TransactionsFormView(SuccessMessageMixin, FormView):
  template_name = 'transaction-form.html'
  form_class = TransactionForm

  success_message = "Transação cadastrada com sucesso!"
  success_url = reverse_lazy('dashboard')

  def get_context_data(self, **kwargs):
      context = super(TransactionsFormView, self).get_context_data(**kwargs)
      context['investor'] = get_investor(request=self.request)

      return context

  def form_valid(self, form):
    form.instance.investor = get_investor(self.request)
    form.save()
    return super().form_valid(form)



def get_investor(request):
    user = User.objects.get(id=request.user.id)
    investor = Investor.objects.get(user=user)

    return investor