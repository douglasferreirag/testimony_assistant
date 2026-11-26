from django.shortcuts import render, redirect
from django.contrib import messages

from testimony.models import Person


def registry_of_person(request):

    if request.method == 'POST':

        person = Person(
            name=request.POST.get('name').strip(),
            contact=request.POST.get('contact').strip()
        )

        print("person.name")

        person.save()

        messages.success(
            request,
            "Pessoa cadastrada com sucesso!",
            extra_tags='person'
        )

        return redirect('registry_of_person')

    return render(
        request,
        'testimony/person/registry/registry_of_person.html'
    )
