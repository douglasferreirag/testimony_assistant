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

        return redirect("list_of_letters")

    return render(
        request,
        "testimony/registry_of_letter.html"
    )