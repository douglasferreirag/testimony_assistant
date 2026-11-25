from django.shortcuts import (
    render,
    redirect
)

from testimony.models import (
    Study,
    Conversation,
    Publication
)


def registry_of_study(request):

    if request.method == 'POST':

        conversation = Conversation.objects.get(
            id=request.POST.get(
                'conversation_id'
            )
        )

        publication = Publication.objects.get(
            id=request.POST.get(
                'publication_id'
            )
        )

        study = Study(
            conversation=conversation,
            publication=publication,
            where_to_continue=request.POST.get(
                'where_to_continue'
            )
        )

        study.save()

        return redirect(
            'list_of_studies'
        )

    conversations = (
        Conversation.objects.all()
    )

    publications = (
        Publication.objects.all()
    )

    return render(
        request,
        'testimony/study/registry/registry_of_study.html',
        {
            'conversations': conversations,
            'publications': publications
        }
    )
