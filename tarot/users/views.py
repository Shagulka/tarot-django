import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from coins.models import BankAccount
from tarot import settings

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account
from .permissions import CustomLoginRequiredMixin


class SignUpFormView(SuccessMessageMixin, CreateView):
    template_name = 'users/signup.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Вы успешно зарегистрированы'

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
        )
        BankAccount.objects.get_or_create(user=user, balance=0)
        login(self.request, user)
        return redirect(self.success_url)


class ProfileUpdate(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Account
    form_class = AccountChangeForm
    template_name = 'users/profile.html'
    success_message = 'Данные успешно обновлены'
    success_url = reverse_lazy('users:profile')

    def get_client_ip(self):
        return self.request.META.get('REMOTE_ADDR')

    def get_timezone(self):
        ip_address = self.get_client_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        return response.get('timezone')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        timezone = self.get_timezone()
        if timezone:
            form.instance.timezone = timezone
        else:
            form.instance.timezone = settings.TIME_ZONE
        form.save()
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Вы успешно вышли')
        return response
