from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Book  # Замените на свою модель

@receiver(post_save, sender=Book)
def send_notification(sender, instance, created, **kwargs):
    if created:  # Только при создании, не при обновлении
        send_mail(
            "Новая запись добавлена!",
            f"Добавлена новая запись: {instance}",
            "anton43234@gmail.com",
            ["anton43234@gmail.com"],  # Кому отправлять уведомления
            fail_silently=False,
        )

