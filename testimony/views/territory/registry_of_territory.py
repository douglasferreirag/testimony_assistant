from django.shortcuts import (
    render,
    redirect
)

from django.contrib import messages

from testimony.models import Territory


def registry_of_territory(request):

    if request.method == 'POST':

        territory = Territory(
            description=request.POST.get(
                'description', ''
            ).strip(),

            city=request.POST.get(
                'city', ''
            ).strip(),

            reference_point=request.POST.get(
                'reference_point', ''
            ).strip(),

            state=request.POST.get(
                'state', ''
            ).strip()
        )

        territory.save()

        messages.success(
            request,
            'Território cadastrado com sucesso!',
            extra_tags='territory'
        )

        return redirect('registry_of_territory')

    return render(
        request,
        'testimony/territory/registry/registry_of_territory.html'
    )