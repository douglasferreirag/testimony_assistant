"""
URL configuration for testimony_assistant project.
"""

from django.contrib import admin
from django.urls import path

# Homepage
from testimony.views.homepage.homepage import homepage

# Letter
from testimony.views.letter.registry_of_letter import registry_of_letter
from testimony.views.letter.list_of_letters import list_of_letters

# Territory
from testimony.views.territory.registry_of_territory import registry_of_territory
from testimony.views.territory.list_of_territories import list_of_territories

# Letter Delivery
from testimony.views.letterdelivery.registry_of_letter_delivery import registry_of_letter_delivery
from testimony.views.letterdelivery.list_of_letters_deliveries import list_of_letters_deliveries

# Person
from testimony.views.person.registry_of_person import registry_of_person
from testimony.views.person.list_of_persons import list_of_persons

# Conversation
from testimony.views.conversation.registry_of_conversation import registry_of_conversation
from testimony.views.conversation.list_of_conversations import list_of_conversations

# Magazine
from testimony.views.magazine.registry_of_magazine import registry_of_magazine
from testimony.views.magazine.list_of_magazines import list_of_magazines

# Book
from testimony.views.book.registry_of_book import registry_of_book
from testimony.views.book.list_of_books import list_of_books

# Video
from testimony.views.video.registry_of_video import registry_of_video
from testimony.views.video.list_of_videos import list_of_videos

# Leaflet
from testimony.views.leaflet.registry_of_leaflet import registry_of_leaflet
from testimony.views.leaflet.list_of_leaflets import list_of_leaflets

# Study
from testimony.views.study.registry_of_study import registry_of_study
from testimony.views.study.list_of_studies import list_of_studies



urlpatterns = [

    path('admin/', admin.site.urls),

    # Homepage
    path('', homepage, name='homepage'),

    # Cartas
    path('letter/registry/', registry_of_letter, name='registry_of_letter'),
    path('letter/list/', list_of_letters, name='list_of_letters'),

    # Territórios
    path('territory/registry/', registry_of_territory, name='registry_of_territory'),
    path('territory/list/', list_of_territories, name='list_of_territories'),

    # Entregas
    path('letterdelivery/registry/', registry_of_letter_delivery, name='registry_of_letter_delivery'),
    path('letterdelivery/list/', list_of_letters_deliveries, name='list_of_letters_deliveries'),

    #  Pessoas
    path('person/registry/', registry_of_person, name='registry_of_person'),
    path('person/list/', list_of_persons, name='list_of_persons'),

    #  Conversas
    path('conversation/registry/', registry_of_conversation, name='registry_of_conversation'),
    path('conversation/list/', list_of_conversations, name='list_of_conversations'),

    # Revistas
    path('magazine/registry/', registry_of_magazine, name='registry_of_magazine'),
    path('magazine/list/', list_of_magazines, name='list_of_magazines'),

    #  Livros
    path('book/registry/', registry_of_book, name='registry_of_book'),
    path('book/list/', list_of_books, name='list_of_books'),

    # Vídeos
    path('video/registry/', registry_of_video, name='registry_of_video'),
    path('video/list/', list_of_videos, name='list_of_videos'),

    # Folhetos
    path('leaflet/registry/', registry_of_leaflet, name='registry_of_leaflet'),
    path('leaflet/list/', list_of_leaflets, name='list_of_leaflets'),

    # Estudos
    path('study/registry/', registry_of_study, name='registry_of_study'),
    path('study/list/', list_of_studies, name='list_of_studies'),
]