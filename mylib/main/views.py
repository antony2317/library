from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets

from .models import Book, Reservation, Genre
from .serializers import BookSerializer


def index(request):
    latest_books = Book.objects.all().order_by('-published_date')[:3]
    return render(request, 'main/home.html', {'latest_books': latest_books})


def book_catalog(request):
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre__name=genre)
    else:
        books = Book.objects.all()


    genres = Genre.objects.all()

    return render(request, 'main/book_catalog.html', {'books': books, 'genres': genres})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)


    is_booked = book.reservations.filter(expires_at__gt=timezone.now()).exists()

    return render(request, 'main/book_detail.html', {
        'book': book,
        'is_booked': is_booked,
    })

@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)


    active_reservation = Reservation.objects.filter(book=book, expires_at__gt=timezone.now()).first()

    if active_reservation:
        messages.error(request, f"Эта книга уже забронирована пользователем {active_reservation.user.username}.")
    else:
        # Создаем бронирование
        expires_at = timezone.now() + timezone.timedelta(weeks=2)
        reservation = Reservation(book=book, user=request.user, expires_at=expires_at)
        reservation.save()
        messages.success(request, "Книга успешно забронирована на 2 недели.")

    return redirect('book_detail', book_id=book.id)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
