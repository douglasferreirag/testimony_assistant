from django.shortcuts import render


def homepage(request):
    return render(request, "testimony/homepage/homepage.html")