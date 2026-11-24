from django.shortcuts import render, redirect

from testimony.models import Book


def registry_of_book(request):

    if request.method == 'POST':

        book = Book(
            id=request.POST.get('id').strip(),
            description=request.POST.get('descricao').strip(),
            year=int(request.POST.get('ano')),
            chapter_quantity=int(
                request.POST.get('capitulos')
            )
        )

        book.save()

        return redirect('registry_of_book')

    return render(
        request,
        'testimony/registry_of_book.html'
    )