from django.shortcuts import render
# futuramente você pode importar os models
# from .models import Carta, Territorio, Pessoa, Entrega, Conversa, Revista, Video, Livro

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

def list_of_territories(request):
    return render(request, 'testimony/list_of_territories.html')

def list_of_letters_deliveries(request):
    return render(request, 'testimony/list_of_letters_deliveries.html')

def registry_of_conversations(request):
    return render(request, 'testimony/registry_of_conversations.html')

def list_of_conversations(request):
    return render(request, 'testimony/list_of_conversations.html')

# Agora trocamos Publicações por Revistas
def registry_of_magazines(request):
    return render(request, 'testimony/registry_of_magazines.html')

def registry_of_videos(request):
    return render(request, 'testimony/registry_of_videos.html')

def list_of_videos(request):
    return render(request, 'testimony/list_of_videos.html')

def registry_of_books(request):
    return render(request, 'testimony/registry_of_books.html')
