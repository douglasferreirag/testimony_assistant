
from django.shortcuts import render, redirect
from django.contrib import messages

from testimony.models import (
    Conversation,
    Person,
    Territory
)


def registry_of_conversation(request):

    if request.method == "POST":

        person = Person.objects.get(
            id=request.POST.get("person_id")
        )

        territory = Territory.objects.get(
            id=request.POST.get("territory_id")
        )

        conversation = Conversation(
            person=person,
            territory=territory,
            conversation_date=request.POST.get(
                "conversation_date"
            )
        )

        conversation.save()

        messages.success(
            request,
            "Conversa cadastrada com sucesso!",
            extra_tags="conversation"
        )

        return redirect("registry_of_conversation")

    persons = Person.objects.all()

    territories = Territory.objects.all()

    return render(
        request,
        "testimony/conversation/registry/registry_of_conversation.html",
        {
            "persons": persons,
            "territories": territories
        }
    )
