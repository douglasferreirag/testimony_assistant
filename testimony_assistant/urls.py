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
    list_of_letters_deliveries,   # nova view para listagem de entregas
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
]
