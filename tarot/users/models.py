from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail

from .managers import CustomAccountManager


class Account(AbstractUser):
    class GenderTypes(models.IntegerChoices):
        FEMALE = 1, 'женщина'
        MALE = 2, 'мужчина'

    username = None
    first_name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)
    email = models.EmailField(
        'адрес электронной почты',
        unique=True
    )
    date_of_birth = models.DateField(
        null=True
    )
    custom_username = models.SlugField(
        'ник',
        unique=True,
        null=True,
        max_length=50,
        help_text='Максимальная длина 50 символов'
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
    profile_picture = models.ImageField(
        'картинка',
        null=True,
        blank=True,
        upload_to='uploads/%Y/%m/'
    )
    timezone = models.CharField(
        'часовой пояс',
        max_length=5,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    gender_choices = dict(GenderTypes.choices)

    def get_zodiac_sign(self):
        if self.date_of_birth:
            day, month = self.date_of_birth.day, self.date_of_birth.month

            if month == 12:
                return 9 if (day < 22) else 10
            elif month == 1:
                return 10 if (day < 20) else 11
            elif month == 2:
                return 11 if (day < 19) else 12
            elif month == 3:
                return 12 if (day < 21) else 1
            elif month == 4:
                return 1 if (day < 20) else 2
            elif month == 5:
                return 2 if (day < 21) else 3
            elif month == 6:
                return 3 if (day < 21) else 4
            elif month == 7:
                return 4 if (day < 23) else 5
            elif month == 8:
                return 5 if (day < 23) else 6
            elif month == 9:
                return 6 if (day < 23) else 7
            elif month == 10:
                return 7 if (day < 23) else 8
            elif month == 11:
                return 8 if (day < 22) else 9

    def zodiac_sign(self):
        zodiac_dict = {
            1: 'Овен',
            2: ' Телец',
            3: ' Близнецы',
            4: ' Рак',
            5: ' Лев',
            6: ' Дева',
            7: ' Весы',
            8: ' Скорпион',
            9: ' Стрелец',
            10: ' Козерог',
            11: ' Водолей',
            12: ' Рыбы'
        }
        return zodiac_dict.get(self.get_zodiac_sign)

    @property
    def get_profile_pic(self):
        return get_thumbnail(
            self.profile_picture,
            '200x200',
            crop='center',
            quality=31
        )

    def img_tmb(self):
        if self.profile_picture:
            return mark_safe('<img src="%s"' % self.get_profile_pic.url)
        return 'Нет изображения'

    img_tmb.allow_tags = True
    img_tmb.short_description = 'аватар'

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
