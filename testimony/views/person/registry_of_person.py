from django.shortcuts import (
    render,
    redirect
)

from testimony.models import Person


def registry_of_person(request):

    if request.method == 'POST':

        person = Person(
            name=request.POST.get(
                'name'
            ),
            contact=request.POST.get(
                'contact'
            )
        )

        person.save()

   

    return render(
        request,
        'testimony/person/registry/registry_of_person.html'
    )