from django.shortcuts import render

from testimony.models import Video


def list_of_videos(request):

    videos = (
        Video.objects
        .order_by('description')
    )

    return render(
        request,
        'video/list_of_videos.html',
        {
            'videos': videos
        }
    )
