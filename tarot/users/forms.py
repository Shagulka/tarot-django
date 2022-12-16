from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = (Account.email.field.name,)


class AccountChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Account
        fields = (Account.first_name.field.name,
                  Account.last_name.field.name,
                  Account.custom_username.field.name,
                  Account.bio.field.name,
                  Account.date_of_birth.field.name,
                  Account.gender.field.name
                  )
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Ник',
            'date_of_birth': 'Дата рождения',
            'bio': 'Био',
            'gender': 'Пол',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'},
                                             format='%Y-%m-%d'),
            'gender': forms.Select(attrs={'class': 'form-select'},
                                   choices=Account.GenderTypes.choices),
        }
        help_texts = {
            'first_name': 'Укажите ваше имя',
            'last_name': 'Укажите вашу фамилию',
            'gender': 'Укажите свой пол',
            'date_of_birth': 'Введите дату в формате ДД.ММ.ГГГГ',
        }
