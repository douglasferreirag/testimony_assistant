from django.db import models

from .publication import Publication


class Leaflet(Publication):

    LARGE = 'LARGE'
    SMALL = 'SMALL'

    SIZE_CHOICES = (
        (LARGE, 'Large'),
        (SMALL, 'Small')
    )

    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES
    )

    class Meta:
        db_table = 'leaflet'
        verbose_name = 'Leaflet'
        verbose_name_plural = 'Leaflets'