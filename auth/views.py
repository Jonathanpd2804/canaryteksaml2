from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return HttpResponse("Hola, mundo!")

def home(request):
    return HttpResponse("Bienvenido a mi aplicación Django!")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from djangosaml2.backends import Saml2Backend


# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



