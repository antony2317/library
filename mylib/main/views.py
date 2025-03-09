from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Book, Reservation


def index(request):
    latest_books = Book.objects.all().order_by('-published_date')[:3]
    return render(request, 'main/home.html', {'latest_books': latest_books})


def book_catalog(request):
    books = Book.objects.all()
    return render(request, 'main/book_catalog.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Проверяем, есть ли активные бронирования для этой книги
    is_booked = book.reservations.filter(expires_at__gt=timezone.now()).exists()

    return render(request, 'main/book_detail.html', {
        'book': book,
        'is_booked': is_booked,  # Передаем результат в шаблон
    })

@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Проверяем, не забронирована ли книга уже
    if Reservation.objects.filter(book=book, expires_at__gt=timezone.now()).exists():
        messages.error(request, "Эта книга уже забронирована.")
    else:
        # Создаем бронирование
        reservation = Reservation(book=book, user=request.user)
        reservation.save()
        messages.success(request, "Книга успешно забронирована на 2 недели.")

    return redirect('book_detail', book_id=book.id)
