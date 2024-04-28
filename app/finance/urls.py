from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name= 'index'),
   path('client_details/<int:client_id>', views.client_details, name='client_details'),# http://127.0.0.1:8000/finance/client_details/1   // cambia el numero por cada cliente,su id
   path('client_details/', views.client_details_default, name='client_details_default'),# http://127.0.0.1:8000/finance/client_details/1
   path('client_details_default', views.client_details_default, name='client_details_default'),#http://127.0.0.1:8000/finance/client_details/1
   path('all_transactions', views.all_transactions, name='all_transactions'),  # http://127.0.0.1:8000/finance/all_transactions

]
