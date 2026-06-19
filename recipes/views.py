from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Douglas',
    })

def sobre(request):
    return HttpResponse("Informações sobre a empresa.")

def contato(request):
    return HttpResponse("Entre em contato conosco.")