from django.db.models import signals

from coins.models import BankAccount
from tarot import settings


def create_bank_account(sender, instance, created, **kwargs):
    """Создание банковского счета для каждого пользователя"""
    if created:
        BankAccount.objects.get_or_create(user=instance, balance=0)


signals.post_save.connect(
    create_bank_account,
    sender=settings.AUTH_USER_MODEL,
    weak=False,
    dispatch_uid='models.create_bank_account'
)
