from django.shortcuts import render

from testimony.models import Study


def list_of_studies(request):

    studies = (
        Study.objects
        .select_related(
            'conversation',
            'publication'
        )
    )

    return render(
        request,
        'testimony/study/list/list_of_studies.html',
        {
            'studies': studies
        }
    )
