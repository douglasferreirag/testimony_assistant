from django.db import models

from .publication import Publication


class Video(Publication):

    duration = models.DurationField()

    def __str__(self):
        return self.description
