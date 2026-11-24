from django.shortcuts import (
    render,
    redirect
)

from testimony.models import (
    Delivery,
    Letter,
    Territory
)


def registry_of_letter_delivery(request):

    if request.method == 'POST':

        letter = Letter.objects.get(
            id=request.POST.get(
                'id_letter'
            )
        )

        territory = Territory.objects.get(
            id=request.POST.get(
                'id_territory'
            )
        )

        delivery = Delivery(
            letter=letter,
            territory=territory,
            delivery_date=request.POST.get(
                'delivery_date'
            ),
            location=request.POST.get(
                'location'
            )
        )

        delivery.save()

        return redirect(
            'registry_of_delivery'
        )

    letters = Letter.objects.all()

    territories = Territory.objects.all()

    return render(
        request,
        'testimony/registry_of_delivery.html',
        {
            'letters': letters,
            'territories': territories
        }
    )