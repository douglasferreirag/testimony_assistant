from django.shortcuts import render

from testimony.models import Magazine


def list_of_magazines(request):

    magazines = Magazine.objects.order_by(
        'description'
    )

    return render(
        request,
        'testimony/magazine/list/list_of_magazines.html',
        {
            'magazines': magazines
        }
    )