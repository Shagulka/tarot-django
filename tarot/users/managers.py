from django.contrib.auth.base_user import BaseUserManager

from coins.models import BankAccount


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Электронная почта должна быть указана')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        BankAccount.objects.get_or_create(user=user, balance=0)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперюзер должен иметь атрибут is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперюзер должен иметь атрибут is_superuser=True.'
            )
        return self.create_user(email, password, **extra_fields)
