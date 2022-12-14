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
    title_for_main_page = models.CharField(
        'название для главной страницы',
        max_length=150,
        null=True,
        help_text=('Название гадания, которое будет '
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
        help_text=('Название гадания, которое будет '
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

    @property
    def number_of_cards(self) -> int:
        if self.type_fortune_telling == self.TypesAlignment.TAROT_1:
            return 1
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_2:
            return 2
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_3:
            return 3
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_4:
            return 4
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_2_3:
            return 5
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_3_3:
            return 6
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_H:
            return 7
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_STAR:
            return 5
        elif self.type_fortune_telling == self.TypesAlignment.TAROT_9:
            return 9

    class TypesFortune(models.IntegerChoices):
        REGULAR = 1, 'Обычное'
        LOVE = 2, 'Любовное'
        MONEY = 3, 'Денежное'
        WORK = 4, 'Работа'
        DAY = 5, 'День'

    default_card_description = models.IntegerField(
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
