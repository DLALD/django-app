from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("::: WELCOME TO MY SITE :::")

def list_users(request):
    users = User.objects.all()
    print(users)  # Verifica que esto imprima los usuarios en la consola
    return render(request, 'academics/list_user.html', {'users': users})

def create_user(request):
    return HttpResponse("Here you find a list of people")
