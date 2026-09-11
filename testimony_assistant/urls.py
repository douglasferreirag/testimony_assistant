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
    registry_of_peoples,
    registry_of_territories,
    registry_of_peoples,   # nova view para pessoas
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('carta/registry/', registry_of_letters, name='registry_of_letters'),
    path('territorio/registry/', registry_of_territories, name='registry_of_territories'),
    path('entrega/registry/', registry_of_letters_deliveries, name='registry_of_letters_deliveries'),
    path('pessoa/registry/', registry_of_peoples, name='registry_of_peoples'),  # nova rota
]
