from django.shortcuts import render, redirect

from testimony.models import Letter


def registry_of_letter(request):

    if request.method == "POST":

        letter = Letter(
            id=request.POST.get("id"),
            description=request.POST.get("description"),
            base=request.POST.get("base")
        )

        letter.save()

        

    return render(
        request,
        "testimony/letter/registry/registry_of_letter.html"
    )