# views/register_video.py

from django.shortcuts import (
    render,
    redirect
)

from testimony.models import Video


def registry_of_video(request):

    if request.method == 'POST':

        video = Video(
            id=request.POST.get('id'),
            description=request.POST.get(
                'description'
            ),
            year=int(
                request.POST.get('year')
            ),
            duration=request.POST.get(
                'duration'
            )
        )

        video.save()

        return redirect(
            'list_of_videos'
        )

    return render(
        request,
        'testimony/registry_of_video.html'
    )