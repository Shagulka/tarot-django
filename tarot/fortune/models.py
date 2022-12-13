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
        'название гадания',
        max_length=150,
        default='Название для админки и т.д.',
    )
    slug = models.SlugField(
        'идентификатор',
        unique=True,
        null=True,
        max_length=200,
        help_text='Максимальная длина 200 символов'
    )
    title_for_main_page = models.CharField(
        'название для главной страницы',
        max_length=150,
        null=True,
        help_text=('Название гадания, которое будет ',
                   'отображаться на главной странице')
    )

    fortune_description = models.TextField(
        'описание карточки с гаданием',
        default='Описание',
        help_text='Описание карточки с гаданием в главном меню'
    )

    title_for_fortune = models.CharField(
        'название гадания',
        max_length=150,
        blank=True,
        help_text=('Название гадания, которое будет ',
                   'отображаться на странице гадания')
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

    type_fortune_telling = models.IntegerField(
        'тип гадания',
        choices=TypesAlignment.choices,
        default=TypesAlignment.TAROT_1,
        help_text='Тип гадания'
    )

    number_of_cards = models.IntegerField(
        'количество карт',
        default=1,
        validators=[MinValueValidator(1)],
        help_text=('Количество карт в гадании ',
                   '(пожалуйста, убедитесь, что количество карт ',
                   'соответствует типу гадания)')
    )

    title_for_cards = models.ManyToManyField(
        CardTitle,
        verbose_name='тайтлы для карт',
        # TODO validate that the number
        # of cards is equal to the type of fortune
        help_text=('Тайтлы для карт ',
                   '(типа ПРОШЛОЕ, НАСТОЯЩЕЕ, БУДУЩЕЕ)')
    )

    class TypesFortune(models.IntegerChoices):
        REGULAR = 1, 'Обычное'
        LOVE = 2, 'Любовное'
        MONEY = 3, 'Денежное'
        WORK = 4, 'Работа'
        DAY = 5, 'День'

    default_card_description = models.TextField(
        'тип гадания',
        choices=TypesFortune.choices,
        default=TypesFortune.REGULAR,
        help_text=('Тип гадания (какое описание ',
                   'карты будет по умолчанию)')
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
