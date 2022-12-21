from django.core.validators import MinValueValidator
from django.db import models

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
        return f'счет пользователя {self.user}'

    class Meta:
        verbose_name = 'пользовательский счет'
        verbose_name_plural = 'пользовательские счета'
