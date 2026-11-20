from django.db import models

from .publication import Publication


class Book(Publication):

    chapter_quantity = models.IntegerField()

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'