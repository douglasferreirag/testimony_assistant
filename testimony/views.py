from django.shortcuts import render
# futuramente você pode importar os models
# from .models import Carta, Territorio, Pessoa, Entrega, Conversa, Revista, Video, Livro, Leaflet, Study

def homepage(request):
    return render(request, 'testimony/homepage/homepage.html')

# Letters

def registry_of_letter(request):
    return render(request, 'testimony/letters/registry/registry_of_letter.html')

def list_of_letters(request):
    return render(request, 'testimony/letters/list/list_of_letters.html')

# Territories

def registry_of_territory(request):
    return render(request, 'testimony/territories/registry/registry_of_territory.html')

def list_of_territories(request):
    return render(request, 'testimony/territories/list/list_of_territories.html')

# Peoples

def registry_of_people(request):
    return render(request, 'testimony/peoples/registry/registry_of_people.html')

def list_of_peoples(request):
    return render(request, 'testimony/peoples/list/list_of_peoples.html')

# Letters Deliveries

def registry_of_letter_delivery(request):
    return render(request, 'testimony/letters_deliveries/registry/registry_of_letter_delivery.html')

def list_of_letters_deliveries(request):
    return render(request, 'testimony/letters_deliveries/list/list_of_letters_deliveries.html')

# Conversations

def registry_of_conversation(request):
    return render(request, 'testimony/conversations/registry/registry_of_conversation.html')

def list_of_conversations(request):
    return render(request, 'testimony/conversations/list/list_of_conversations.html')

# Magazines

def registry_of_magazine(request):
    return render(request, 'testimony/magazines/registry/registry_of_magazine.html')

def list_of_magazines(request):
    return render(request, 'testimony/magazines/list/list_of_magazines.html')

# Videos

def registry_of_video(request):
    return render(request, 'testimony/videos/registry/registry_of_video.html')

def list_of_videos(request):
    return render(request, 'testimony/videos/list/list_of_videos.html')

# Books
def registry_of_book(request):
    return render(request, 'testimony/books/registry/registry_of_book.html')

def list_of_books(request):
    return render(request, 'testimony/books/list/list_of_books.html')

# Leaflets
def registry_of_leaflet(request):
    return render(request, 'testimony/leaflets/registry/registry_of_leaflet.html')

def list_of_leaflets(request):
    return render(request, 'testimony/leaflets/list/list_of_leaflets.html')

# Studies
def registry_of_study(request):
    return render(request, 'testimony/studies/registry/registry_of_study.html')

def list_of_studies(request):
    return render(request, 'testimony/studies/list/list_of_studies.html')
