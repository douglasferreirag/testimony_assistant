from django.db import models


class Publication(models.Model):

    id = models.CharField(
        primary_key=True,
        max_length=255
    )

    description = models.CharField(
        max_length=255
    )

    year = models.IntegerField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'publication'
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'