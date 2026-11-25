from django.shortcuts import render, redirect
from django.contrib import messages

from testimony.models import Book


def registry_of_book(request):

    if request.method == 'POST':

        book = Book(
            id=request.POST.get('id').strip(),
            description=request.POST.get('description').strip(),
            year=int(request.POST.get('year')),
            chapter_quantity=int(
                request.POST.get('chapter_quantity')
            )
        )

        book.save()

        messages.success(
            request,
            "Livro cadastrado com sucesso!",
            extra_tags="book"
        )

        return redirect('registry_of_book')

    return render(
        request,
        'testimony/book/registry/registry_of_book.html'
    )