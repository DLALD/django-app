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

from django.shortcuts import redirect

def client_details_default(request):
    # Redirigir a los detalles del cliente para un client_id específico
    client_id = 1  # Reemplaza esto con el ID del cliente al que quieres redirigir
    return redirect('client_details', client_id=client_id)


def all_transactions(request):
    """
    Vista para mostrar todas las transacciones de todos los clientes.
    """
    transactions = Transaction.objects.all()
    return render(request, 'finance/all_transactions.html', {'transactions': transactions})
