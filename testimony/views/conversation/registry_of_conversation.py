from django.shortcuts import render, redirect

from testimony.models import (
    Conversation,
    Person,
    Territory
)


def registry_of_conversation(request):

    if request.method == "POST":

        person = Person.objects.get(
            id=request.POST.get("id_pessoa")
        )

        territory = Territory.objects.get(
            id=request.POST.get("id_territorio")
        )

        conversation = Conversation(
            person=person,
            territory=territory,
            conversation_date=request.POST.get(
                "data_conversa"
            )
        )

        conversation.save()

        return redirect(
            "registry_of_conversation"
        )

    persons = Person.objects.all()

    territories = Territory.objects.all()

    return render(
        request,
        "testimony/registry_of_conversation.html",
        {
            "persons": persons,
            "territories": territories
        }
    )