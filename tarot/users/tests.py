from django.test import TestCase

from .forms import AccountChangeForm, AccountCreationForm


class CustomUserCreationFormTest(TestCase):

    def test_invalid_form(self):
        form = AccountCreationForm(data={
            'email': 'example@gg.gg',
            'password': '',
        })
        self.assertFalse(form.is_valid())


class CustomUserChangeFormTest(TestCase):
    def test_valid_form(self):
        form = AccountChangeForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'custom_username': 'john123',
            'bio': 'djlajdlajdajdkal',
            'date_of_birth': '1990-01-05',
            'gender': 1,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = AccountChangeForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'custom_username': 'john123',
            'bio': 'djlajdlajdajdkal',
            'date_of_birth': '1990-01-01-23-23',
            'gender': 2,

        })
        self.assertFalse(form.is_valid())
