from django.shortcuts import (
    render,
    redirect
)

from testimony.models import Territory


def registry_of_territory(request):

    if request.method == 'POST':

        territory = Territory(
            descricao=request.POST.get(
                'descricao'
            ),
            cidade=request.POST.get(
                'cidade'
            ),
            referencia=request.POST.get(
                'referencia'
            ),
            estado=request.POST.get(
                'estado'
            )
        )

        territory.save()

        return redirect(
            'list_of_territories'
        )

    return render(
        request,
        'testimony/registry_of_territory.html'
    )

    