from django.core.validators import MinValueValidator
from django.db import models

from fortune.models import Fortune
from tarot import settings


class BankAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    balance = models.IntegerField(
        'баланс',
        validators=[MinValueValidator(0), ]
    )
    bonus = models.DateTimeField(
        'последнее время получения бонуса',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'пользовательский счет'
        verbose_name_plural = 'пользовательские счета'


class Purchase(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата платежа'
    )
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer')

    fortune = models.OneToOneField(
        Fortune,
        on_delete=models.CASCADE,
        verbose_name='гадание',
        help_text='Выберите гадание'
    )

    def __str__(self):
        return self.fortune

    class Meta:
        verbose_name = 'покупка гадания'
        verbose_name_plural = 'покупки гадания'
