from django.shortcuts import render

from testimony.models import Letter


def list_of_letters(request):
    letters = Letter.objects.all()

    return render(request, "testimony/letter/list/list_of_letters.html", {
        'letters': letters
    })