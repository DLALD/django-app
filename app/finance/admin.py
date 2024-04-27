from django.contrib import admin
from .models import Client, Product, ClientProduct, TransactionType, Transaction

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(ClientProduct)
admin.site.register(TransactionType)
admin.site.register(Transaction)
