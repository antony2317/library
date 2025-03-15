# Generated by Django 4.2.19 on 2025-03-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_reservation_delete_uploadfiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='main.category', verbose_name='Жанр'),
        ),
    ]
