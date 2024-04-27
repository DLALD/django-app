from django.urls import path
from . import views

urlpatterns = [
    path('client_details/<int:client_id>', views.client_details, name='client_details'),
    path('client_details/', views.client_details_default, name='client_details_default'), 
    path('client_details_default', views.client_details_default, name='client_details_default'),  
    path('', views.all_transactions, name='finance'),  # URL raíz para mostrar todas las transacciones
]
