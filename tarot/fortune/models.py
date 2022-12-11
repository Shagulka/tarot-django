from django.core.validators import MinValueValidator
from django.db import models


class CardTitle(models.Model):
    name = models.CharField(
        'название для карт',
        max_length=150,
        default='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тайтл карты'
        verbose_name_plural = 'Тайтлы для карты'


class Fortune(models.Model):
    name = models.CharField(
        'название гадания короткое',
        max_length=150,
        default='Название',
    )
    slug = models.SlugField(
        'идентификатор',
        unique=True,
        default='id-fortune',
        max_length=200,
        help_text='Максимальная длина 200 символов'
    )
    title_for_main_page = models.CharField(
        'название для главной страницы',
        max_length=150,
        default='Название',
    )
    title_for_fortune = models.CharField(
        'название гадания',
        max_length=150,
        default='Название',
    )
    type_fortune_telling = models.PositiveIntegerField(
        'тип гадания',
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        help_text='Тип гадания'
    )
    title_for_cards = models.ManyToManyField(
        CardTitle,
        verbose_name='тайтлы для карт',
    )
    card_description = models.TextField(
        'описание карты',
        default='Описание',
        help_text='Описание карты'
    )
    default_card_description = models.TextField(
        'дефолтное описание карты',
        default='Описание',
        help_text='Дефолтное описание товара'
    )

    number_of_cards = models.PositiveIntegerField(
        'количество карт',
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        help_text='Количество карт в гадании'
    )

    price = models.PositiveIntegerField(
        'цена',
        default=50,
        validators=[
            MinValueValidator(1),
        ],
        help_text='Цена гадания'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'гадание'
        verbose_name_plural = 'Гадания'
