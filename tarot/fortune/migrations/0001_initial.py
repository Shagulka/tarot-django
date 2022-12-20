# Generated by Django 3.2.16 on 2022-12-19 22:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название', max_length=150, verbose_name='название для карт')),
            ],
            options={
                'verbose_name': 'тайтл карты',
                'verbose_name_plural': 'Тайтлы для карты',
            },
        ),
        migrations.CreateModel(
            name='Fortune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название для админки и т.д.', max_length=150, verbose_name='название гадания')),
                ('slug', models.SlugField(help_text='Максимальная длина 200 символов', max_length=200, null=True, unique=True, verbose_name='идентификатор')),
                ('title_for_main_page', models.CharField(help_text='Название гадания, которое будет отображаться на главной странице', max_length=150, null=True, verbose_name='название для главной страницы')),
                ('fortune_description', models.TextField(default='Описание', help_text='Описание карточки с гаданием в главном меню', verbose_name='описание карточки с гаданием')),
                ('title_for_fortune', models.CharField(blank=True, help_text='Название гадания, которое будет отображаться на странице гадания', max_length=150, verbose_name='название гадания')),
                ('type_fortune_telling', models.IntegerField(choices=[(1, 'Таро 1'), (2, 'Таро 2'), (3, 'Таро 3'), (4, 'Таро 4'), (5, 'Таро 2-3'), (6, 'Таро 2-4'), (7, 'Таро 3-4'), (8, 'Таро звезда'), (9, 'Таро 9')], default=1, help_text='Тип гадания', verbose_name='тип гадания')),
                ('number_of_cards', models.IntegerField(default=1, help_text='Количество карт в гадании (пожалуйста, убедитесь, что количество карт соответствует типу гадания)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='количество карт')),
                ('default_card_description', models.IntegerField(choices=[(1, 'Обычное'), (2, 'Любовное'), (3, 'Денежное'), (4, 'Работа'), (5, 'День')], default=1, help_text='Тип гадания (какое описание карты будет по умолчанию)', verbose_name='тип гадания')),
                ('price', models.PositiveIntegerField(default=0, help_text='Цена гадания', validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('title_for_cards', models.ManyToManyField(help_text='Тайтлы для карт (типа ПРОШЛОЕ, НАСТОЯЩЕЕ, БУДУЩЕЕ)', to='fortune.CardTitle', verbose_name='тайтлы для карт')),
            ],
            options={
                'verbose_name': 'гадание',
                'verbose_name_plural': 'Гадания',
            },
        ),
    ]