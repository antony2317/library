import os

import django
from django.core.management.base import BaseCommand
from faker import Faker
from django_seed import Seed
import random

from mylib.main.models import Category, Book

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylib.settings')
django.setup()



class Command(BaseCommand):
    help = 'Генерация фейковых данных для моделей Book и Category'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        fake = Faker('ru_RU')


        category_names = ['Фантастика', 'Детективы', 'Романы', 'Научная литература', 'Приключения']
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name)
            categories.append(category)


        seeder.add_entity(Book, 10, {
            'title': lambda x: fake.sentence(nb_words=3),
            'author': lambda x: fake.name(),
            'description': lambda x: fake.text(max_nb_chars=300),
            'published_date': lambda x: fake.date_between(start_date='-20y', end_date='today'),
            'isbn': lambda x: fake.isbn13(separator="-"),
            'cover_image': None,
            'author_image': None,
        })


        inserted_pks = seeder.execute()


        books = Book.objects.all()
        for book in books:
            book.categories.set(random.sample(categories, random.randint(1, 3)))
            book.save()

        self.stdout.write(self.style.SUCCESS(f'Успешно создано {len(inserted_pks[Book])} книг!'))
