from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(blank=True, verbose_name="Описание")
    published_date = models.DateField(verbose_name="Дата публикации")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Обложка книги")
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name="Обложка автора")
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Жанр")
    reserved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reserved_books')

    def __str__(self):
        return self.title

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    reserved_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(weeks=2)
        super().save(*args, **kwargs)

