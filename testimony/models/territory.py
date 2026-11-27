from django.db import models


class Territory(models.Model):

    description = models.CharField(
        max_length=255
    )

    city = models.CharField(
        max_length=255
    )

    reference_point = models.CharField(
        max_length=255
    )

    state = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'territory'
        verbose_name = 'Territory'
        verbose_name_plural = 'Territories'