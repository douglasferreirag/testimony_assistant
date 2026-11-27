from django.shortcuts import render

from testimony.models import Territory


def list_of_territories(request):

    territories = (
        Territory.objects
        .order_by('description')
    )

    return render(
        request,
        'testimony/territory/list/list_of_territories.html',
        {
            'territories': territories
        }
    )