# Generated by Django 4.2.19 on 2025-03-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('published_date', models.DateField(verbose_name='Дата публикации')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
