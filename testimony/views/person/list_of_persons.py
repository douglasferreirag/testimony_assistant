from django.shortcuts import render

from testimony.models import Person


def list_of_persons(request):

    persons = Person.objects.order_by(
        'name'
    )

    return render(
        request,
        'testimony/list_of_persons.html',
        {
            'persons': persons
        }
    )