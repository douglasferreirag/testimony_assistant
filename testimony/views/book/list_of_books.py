from django.shortcuts import render

from testimony.models import Book

def list_of_books(request):

    books = Book.objects.order_by(
        'description'
    )

    return render(
        request,
        'testimony/list_of_books.html',
        {
            'books': books
        }
    )