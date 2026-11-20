from django.db import models

from .conversation import Conversation
from .publication import Publication


class Study(models.Model):

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE
    )

    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE
    )

    where_to_continue = models.CharField(
        max_length=255
    )

    def __str__(self):
        return (
            f'{self.publication} - '
            f'{self.where_to_continue}'
        )