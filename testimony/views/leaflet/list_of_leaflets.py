from django.shortcuts import render

from testimony.models import Leaflet


def list_of_leaflets(request):

    leaflets = Leaflet.objects.order_by(
        'description'
    )

    return render(
        request,
        'testimony/leaflet/list/list_of_leaflets.html',
        {
            'leaflets': leaflets
        }
    )
