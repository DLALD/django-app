# En urls.py de la aplicación finance

from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_details, name='client_details'),
    path('transactions/', views.all_transactions, name='all_transactions'),
    path('', views.all_transactions, name='finance'),  # URL raíz para mostrar todas las transacciones
    path('', views.client_details, name='client'),  # URL raíz para mostrar todas las transacciones
]
