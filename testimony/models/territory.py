from django.db import models


class Territory(models.Model):

    descricao = models.CharField(
        max_length=255
    )

    cidade = models.CharField(
        max_length=255
    )

    referencia = models.CharField(
        max_length=255
    )

    estado = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'territorio'
        verbose_name = 'Território'
        verbose_name_plural = 'Territórios'