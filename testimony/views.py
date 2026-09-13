from django.shortcuts import render
# futuramente você pode importar o model Carta
# from .models import Carta

def homepage(request):
    return render(request, 'testimony/homepage.html')

def registry_of_letters(request):
    return render(request, 'testimony/registry_of_letters.html')

def registry_of_territories(request):
    return render(request, 'testimony/registry_of_territories.html')

def registry_of_letters_deliveries(request):
    return render(request, 'testimony/registry_of_letters_deliveries.html')

def registry_of_peoples(request):
    return render(request, 'testimony/registry_of_peoples.html')

def list_of_peoples(request):
    return render(request, 'testimony/list_of_peoples.html')

def list_of_letters(request):
    return render(request, 'testimony/list_of_letters.html')
