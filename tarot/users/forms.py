from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

from .models import Account


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Account
        fields = (Account.email.field.name,)
        widgets = {
            Account.email.field.name: forms.TextInput(
                attrs={'class': 'form-control'}
            ),

        }

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не одинаковы")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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
            'name': 'Имя',
            'surname': 'Фамилия',
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
            'name': 'max 255 символов',
            'surname': 'max 255 символов',
            'username': 'max 255 символов',
            'gender': 'Укажите свой пол',
            'date_of_birth': 'Введите дату в формате ДД.ММ.ГГГГ',
        }
