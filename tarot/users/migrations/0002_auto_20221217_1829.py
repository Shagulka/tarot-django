# Generated by Django 3.2.16 on 2022-12-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='account',
            name='custom_username',
            field=models.SlugField(help_text='Максимальная длина 50 символов', null=True, unique=True, verbose_name='ник'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='фамилия'),
        ),
    ]
