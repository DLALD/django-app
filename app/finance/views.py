from django.shortcuts import render
from .models import Client, Transaction

def index(request):
    return render(request, 'finance/index.html')

def client_details(request, client_id):
    """
    Vista para mostrar los detalles de un cliente específico.
    """
    client = Client.objects.get(id=client_id)
    return render(request, 'finance/client_details.html', {'client': client})

def all_transactions(request):
    """
    Vista para mostrar todas las transacciones de todos los clientes.
    """
    transactions = Transaction.objects.all()
    return render(request, 'finance/all_transactions.html', {'transactions': transactions})
