from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account
from .permissions import CustomLoginRequiredMixin, StuffPermissionRequiredMixin


class SignUpFormView(SuccessMessageMixin, CreateView):
    template_name = 'users/signup.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Вы успешно зарегистрированы'

    def form_valid(self, form):
        return super().form_valid(form)
        # user = form.save(commit=False)
        # user.set_password(form.cleaned_data.get('password'))
        # user.save()
        # login(self.request, user)
        # return redirect(self.success_url)


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

    def get_object(self, queryset=None):
        return self.request.user


class UsersListView(
    LoginRequiredMixin,
    ListView
):
    model = Account
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Account.objects.filter(is_active=True)


class UserDetailView(
    LoginRequiredMixin,
    DetailView
):
    model = Account
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
