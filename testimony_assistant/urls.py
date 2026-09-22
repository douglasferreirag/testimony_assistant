"""
URL configuration for testimony_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from testimony.views import (
    homepage,
    list_of_territories,
    registry_of_letter,
    registry_of_letter_delivery,
    registry_of_territory,
    registry_of_people,
    list_of_peoples,
    list_of_letters,
    list_of_territories,
    list_of_letters_deliveries,
    registry_of_conversation,
    list_of_conversations,
    registry_of_magazine,      # view para cadastro de revistas
    list_of_magazines,          # view para listagem de revistas
    registry_of_video,         # view para cadastro de vídeos
    list_of_videos,             # view para listagem de vídeos
    registry_of_book,          # view para cadastro de livros
    list_of_books,              # view para listagem de livros
    registry_of_leaflet,       # view para cadastro de folhetos
    list_of_leaflets,           # view para listagem de folhetos
    registry_of_study,        # view para cadastro de estudos
    list_of_studies,            # view para listagem de estudos
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),

    # Cartas
    path('carta/registry/', registry_of_letter, name='registry_of_letter'),
    path('carta/list/', list_of_letters, name='list_of_letters'),

    # Territórios
    path('territorio/registry/', registry_of_territory, name='registry_of_territory'),
    path('territorio/list/', list_of_territories, name='list_of_territories'),

    # Entregas
    path('entrega/registry/', registry_of_letter_delivery, name='registry_of_letter_delivery'),
    path('entrega/list/', list_of_letters_deliveries, name='list_of_letters_deliveries'),

    # Pessoas
    path('pessoa/registry/', registry_of_people, name='registry_of_people'),
    path('pessoa/list/', list_of_peoples, name='list_of_peoples'),

    # Conversas
    path('conversa/registry/', registry_of_conversation, name='registry_of_conversation'),
    path('conversa/list/', list_of_conversations, name='list_of_conversations'),

    # Revistas
    path('revista/registry/', registry_of_magazine, name='registry_of_magazine'),
    path('revista/list/', list_of_magazines, name='list_of_magazines'),

    # Livros
    path('livro/registry/', registry_of_book, name='registry_of_book'),
    path('livro/list/', list_of_books, name='list_of_books'),

    # Vídeos
    path('video/registry/', registry_of_video, name='registry_of_video'),
    path('video/list/', list_of_videos, name='list_of_videos'),

    # Folhetos (Leaflets)
    path('leaflet/registry/', registry_of_leaflet, name='registry_of_leaflet'),
    path('leaflet/list/', list_of_leaflets, name='list_of_leaflets'),

    # Estudos (Studies)
    path('study/registry/', registry_of_study, name='registry_of_study'),
    path('study/list/', list_of_studies, name='list_of_studies'),
]
