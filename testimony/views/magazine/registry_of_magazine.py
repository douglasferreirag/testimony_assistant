from django.shortcuts import (
    render,
    redirect
)

from testimony.models import Magazine


def registry_of_magazine(request):

    if request.method == 'POST':

        magazine = Magazine(
            id=request.POST.get('id'),
            description=request.POST.get(
                'description'
            ),
            year=int(
                request.POST.get('year')
            ),
            type=request.POST.get(
                'type'
            )
        )

        magazine.save()

      

    return render(
        request,
        'testimony/magazine/registry/registry_of_magazine.html'
    )