from django.shortcuts import render

from testimony.models import Delivery


def list_of_letters_deliveries(request):

    deliveries = (
        Delivery.objects
        .select_related(
            'letter',
            'territory'
        )
    )

    return render(
        request,
        'testimony/list_of_letters_deliveries.html',
        {
            'deliveries': deliveries
        }
    )