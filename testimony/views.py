from django.shortcuts import render
# futuramente você pode importar os models
# from .models import Carta, Territorio, Pessoa, Entrega, Conversa, Revista, Video, Livro, Leaflet, Study

def homepage(request):
    return render(request, 'testimony/homepage.html')

# Letters

def registry_of_letters(request):
    return render(request, 'testimony/letters/registry_of_letters.html')

def list_of_letters(request):
    return render(request, 'testimony/letters/list_of_letters.html')

# Territories

def registry_of_territories(request):
    return render(request, 'testimony/territories/registry_of_territories.html')

def list_of_territories(request):
    return render(request, 'testimony/territories/list_of_territories.html')

# Peoples

def registry_of_peoples(request):
    return render(request, 'testimony/peoples/registry_of_peoples.html')

def list_of_peoples(request):
    return render(request, 'testimony/peoples/list_of_peoples.html')

# Letters Deliveries

def registry_of_letters_deliveries(request):
    return render(request, 'testimony/letters_deliveries/registry_of_letters_deliveries.html')

def list_of_letters_deliveries(request):
    return render(request, 'testimony/letters_deliveries/list_of_letters_deliveries.html')

# Conversations

def registry_of_conversation(request):
    return render(request, 'testimony/conversations/registry/registry_of_conversation.html')

def list_of_conversations(request):
    return render(request, 'testimony/conversations/list_of_conversations.html')

# Magazines

def registry_of_magazines(request):
    return render(request, 'testimony/magazines/registry_of_magazines.html')

def list_of_magazines(request):
    return render(request, 'testimony/magazines/list_of_magazines.html')

# Videos

def registry_of_videos(request):
    return render(request, 'testimony/videos/registry_of_videos.html')

def list_of_videos(request):
    return render(request, 'testimony/videos/list_of_videos.html')

# Books
def registry_of_book(request):
    return render(request, 'testimony/books/registry/registry_of_book.html')

def list_of_books(request):
    return render(request, 'testimony/books/list/list_of_books.html')

# Leaflets
def registry_of_leaflets(request):
    return render(request, 'testimony/leaflets/registry_of_leaflets.html')

def list_of_leaflets(request):
    return render(request, 'testimony/leaflets/list_of_leaflets.html')

# Studies
def registry_of_studies(request):
    return render(request, 'testimony/studies/registry_of_studies.html')

def list_of_studies(request):
    return render(request, 'testimony/studies/list_of_studies.html')
