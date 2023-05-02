from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('dashboard/', login_required(views.DashboardTemplateView.as_view()), name='dashboard'),
    path('transactions/', login_required(views.TransactionsTemplateView.as_view()), name='transactions'),
    path('new-transaction/', login_required(views.TransactionsFormView.as_view()), name='new-transaction'),
    path('transactions/<int:pk>/', login_required(views.TransactionDetailView.as_view()), name='transaction-details'),
    path('transactions/<int:pk>/delete', login_required(views.TransactionDeleteView.as_view()), name='delete-transaction'),
    path('transactions/<int:pk>/update', login_required(views.TransactionUpdateView.as_view()), name='update-transaction'),

]