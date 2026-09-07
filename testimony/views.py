from django.shortcuts import render

def homepage(request):
    return render(request, 'testimony/homepage.html')

def registry_of_letters(request):
    return render(request, 'testimony/registry_of_letters.html')

def registry_of_territories(request):
    return render(request, 'testimony/registry_of_territories.html')

def registry_of_letters_deliveries(request):
    return render(request, 'testimony/registry_of_letters_deliveries.html')
