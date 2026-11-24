# views/list_publication.py

from django.shortcuts import render

from testimony.models import Publication


def list_of_publications(request):

    publications = (
        Publication.objects
        .order_by('description')
    )

    return render(
        request,
        'testimony/list_of_publications.html',
        {
            'publications': publications
        }
    )