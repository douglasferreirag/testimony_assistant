from django.shortcuts import render, redirect

from testimony.models import Leaflet

from django.shortcuts import (
    render,
    redirect
)

from testimony.models import Leaflet


def registry_of_leaflet(request):

    if request.method == 'POST':

        leaflet = Leaflet(
            id=request.POST.get('id'),
            description=request.POST.get(
                'description'
            ),
            year=int(
                request.POST.get('year')
            ),
            size=request.POST.get('size')
        )

        leaflet.save()

       

    return render(
        request,
        'testimony/leaflet/registry/registry_of_leaflet.html'
    )