from django.shortcuts import render

from testimony.models import Conversation


def list_of_conversations(request):

    conversations = Conversation.objects.all()

    return render(
        request,
        'testimony/list_of_conversations.html',
        {
            'conversations': conversations
        }
    )