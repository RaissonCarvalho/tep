from django.contrib import admin
from my_wallet.models import Stock, Transaction
# Register your models here.

admin.site.register(Stock)
admin.site.register(Transaction)
