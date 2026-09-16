"""
URL configuration for testimony_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from testimony.views import (
    homepage,
    registry_of_letters,
    registry_of_letters_deliveries,
    registry_of_territories,
    registry_of_peoples,
    list_of_peoples,
    list_of_letters,
    list_of_territories,
    list_of_letters_deliveries,
    registry_of_conversations,
    list_of_conversations,
    registry_of_magazines,      # view para cadastro de revistas
    list_of_magazines,          # view para listagem de revistas
    registry_of_videos,         # view para cadastro de vídeos
    list_of_videos,             # view para listagem de vídeos
    registry_of_books,          # view para cadastro de livros
    list_of_books,              # view para listagem de livros
    registry_of_leaflets,       # view para cadastro de folhetos
    list_of_leaflets,           # view para listagem de folhetos
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),

    # Cartas
    path('carta/registry/', registry_of_letters, name='registry_of_letters'),
    path('carta/list/', list_of_letters, name='list_of_letters'),

    # Territórios
    path('territorio/registry/', registry_of_territories, name='registry_of_territories'),
    path('territorio/list/', list_of_territories, name='list_of_territories'),

    # Entregas
    path('entrega/registry/', registry_of_letters_deliveries, name='registry_of_letters_deliveries'),
    path('entrega/list/', list_of_letters_deliveries, name='list_of_letters_deliveries'),

    # Pessoas
    path('pessoa/registry/', registry_of_peoples, name='registry_of_peoples'),
    path('pessoa/list/', list_of_peoples, name='list_of_peoples'),

    # Conversas
    path('conversa/registry/', registry_of_conversations, name='registry_of_conversations'),
    path('conversa/list/', list_of_conversations, name='list_of_conversations'),

    # Revistas
    path('revista/registry/', registry_of_magazines, name='registry_of_magazines'),
    path('revista/list/', list_of_magazines, name='list_of_magazines'),

    # Livros
    path('livro/registry/', registry_of_books, name='registry_of_books'),
    path('livro/list/', list_of_books, name='list_of_books'),

    # Vídeos
    path('video/registry/', registry_of_videos, name='registry_of_videos'),
    path('video/list/', list_of_videos, name='list_of_videos'),

    # Folhetos (Leaflets)
    path('leaflet/registry/', registry_of_leaflets, name='registry_of_leaflets'),
    path('leaflet/list/', list_of_leaflets, name='list_of_leaflets'),
]
