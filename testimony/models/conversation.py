from django.db import models

from .person import Person
from .territory import Territory


class Conversation(models.Model):

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

    territory = models.ForeignKey(
        Territory,
        on_delete=models.CASCADE
    )

    conversation_date = models.DateField()

    def __str__(self):
        return f'{self.person} - {self.conversation_date}'

    class Meta:
        db_table = 'conversation'
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'