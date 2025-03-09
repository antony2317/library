from django.contrib import admin
from .models import Book, Category

admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
