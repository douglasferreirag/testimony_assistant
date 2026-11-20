from django.db import models

from .letter import Letter
from .territory import Territory


class Delivery(models.Model):

    letter = models.ForeignKey(
        Letter,
        on_delete=models.CASCADE
    )

    territory = models.ForeignKey(
        Territory,
        on_delete=models.CASCADE
    )

    delivery_date = models.DateField()

    location = models.CharField(
        max_length=255
    )

    def __str__(self):
        return (
            f'{self.letter} - '
            f'{self.delivery_date}'
        )