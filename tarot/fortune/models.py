from django.core.validators import MinValueValidator
from django.db import models


class Fortune(models.Model):
    name = models.CharField(
        'название гадания',
        max_length=150,
        help_text='Название для админки и т.д.',
    )
    slug = models.SlugField(
        'идентификатор',
        unique=True,
        null=True,
        max_length=200,
        help_text='Максимальная длина 200 символов'
    )
    title = models.CharField(
        'название для главной страницы',
        max_length=150,
        null=True,
        help_text=('Название гадания, которое будет '
                   'отображаться на главной странице')
    )

    description = models.TextField(
        'описание карточки с гаданием',
        default='Описание',
        help_text='Описание карточки с гаданием в главном меню'
    )

    title_for_AI = models.CharField(
        'название гадания для ИИ',
        max_length=150,
        blank=True,
        help_text=('Название гадания, которое будет '
                   'использоваться в ИИ '
                   '(по умолчанию используется '
                   'гадание для главной страницы)')
    )

    class TypesAlignment(models.IntegerChoices):
        TAROT_1 = 1, 'Таро 1'
        TAROT_2 = 2, 'Таро 2'
        TAROT_3 = 3, 'Таро 3'
        TAROT_4 = 4, 'Таро 4'
        TAROT_2_3 = 5, 'Таро 2-3'
        TAROT_3_3 = 6, 'Таро 2-4'
        TAROT_H = 7, 'Таро 3-4'
        TAROT_STAR = 8, 'Таро звезда'
        TAROT_9 = 9, 'Таро 9'

    alignment = models.IntegerField(
        'тип гадания',
        choices=TypesAlignment.choices,
        default=TypesAlignment.TAROT_1,
        help_text='Тип гадания'
    )

    @property
    def number_of_cards(self) -> int:
        return {
            self.TypesAlignment.TAROT_1: 1,
            self.TypesAlignment.TAROT_2: 2,
            self.TypesAlignment.TAROT_3: 3,
            self.TypesAlignment.TAROT_4: 4,
            self.TypesAlignment.TAROT_2_3: 5,
            self.TypesAlignment.TAROT_3_3: 6,
            self.TypesAlignment.TAROT_H: 7,
            self.TypesAlignment.TAROT_STAR: 5,
            self.TypesAlignment.TAROT_9: 9,
        }[self.alignment]

    class TypesFortune(models.IntegerChoices):
        REGULAR = 1, 'Обычное'
        LOVE = 2, 'Любовное'
        MONEY = 3, 'Денежное'
        WORK = 4, 'Работа'
        DAY = 5, 'День'

    type = models.IntegerField(
        'тип гадания',
        choices=TypesFortune.choices,
        default=TypesFortune.REGULAR,
        help_text=('Тип гадания (какое описание карты будет по умолчанию)')
    )

    price = models.PositiveIntegerField(
        'цена',
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Цена гадания'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'гадание'
        verbose_name_plural = 'Гадания'
