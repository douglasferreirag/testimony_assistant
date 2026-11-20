from django.db import models

from .publication import Publication


class Magazine(Publication):

    AWAKE = 'AWAKE'
    WATCHTOWER = 'WATCHTOWER'

    TYPE_CHOICES = (
        (AWAKE, 'Awake!'),
        (WATCHTOWER, 'The Watchtower')
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    class Meta:
        db_table = 'magazine'