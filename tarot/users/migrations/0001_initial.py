# Generated by Django 3.2.16 on 2022-12-21 21:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='адрес электронной почты')),
                ('date_of_birth', models.DateField(null=True)),
                ('custom_username', models.SlugField(blank=True, help_text='Максимальная длина 50 символов', null=True, unique=True, verbose_name='ник')),
                ('bio', models.CharField(blank=True, help_text='Максимальная длина 200 символов', max_length=200, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'женщина'), (2, 'мужчина')], default=1, help_text='Ваш пол', verbose_name='пол')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='картинка')),
                ('timezone', models.CharField(max_length=5, null=True, verbose_name='часовой пояс')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]
