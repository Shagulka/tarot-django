from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomAccountManager


class Account(AbstractUser):
    class GenderTypes(models.IntegerChoices):
        FEMALE = 1, 'женщина'
        MALE = 2, 'мужчина'

    username = None
    email = models.EmailField(
        'адрес электронной почты',
        unique=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    custom_username = models.SlugField(
        'ник',
        unique=True,
        null=True,
        max_length=200,
        help_text='Максимальная длина 200 символов'
    )
    bio = models.CharField(
        null=True,
        max_length=200,
        help_text='Максимальная длина 200 символов'
    )

    gender = models.IntegerField(
        'пол',
        choices=GenderTypes.choices,
        default=GenderTypes.FEMALE,
        help_text='Ваш пол'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    def get_zodiac_sign(self):
        day, month = self.date_of_birth.day, self.date_of_birth.month

        if month == 12:
            return 'Стрелец' if (day < 22) else 'Козерог'
        elif month == 1:
            return 'Козерог' if (day < 20) else 'Водолей'
        elif month == 2:
            return 'Водолей' if (day < 19) else 'Рыбы'
        elif month == 3:
            return 'Рыбы' if (day < 21) else 'Овен'
        elif month == 4:
            return 'Овен' if (day < 20) else 'Телец'
        elif month == 5:
            return 'Телец' if (day < 21) else 'Близнецы'
        elif month == 6:
            return 'Близнецы' if (day < 21) else 'Рак'
        elif month == 7:
            return 'Рак' if (day < 23) else 'Лев'
        elif month == 8:
            return 'Лев' if (day < 23) else 'Дева'
        elif month == 9:
            return 'Дева' if (day < 23) else 'Весы'
        elif month == 10:
            return 'Весы' if (day < 23) else 'Скорпион'
        elif month == 11:
            return 'Скорпион' if (day < 22) else 'Стрелец'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
