from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'button_text': 'Iniciar Sesión'
    }
    return render(request, 'home.html', context)






