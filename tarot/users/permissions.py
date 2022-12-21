from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = 'Вы не авторизованы!'
    permission_denied_redirect_url = 'users:login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                'Вы не авторизованы!',
                extra_tags='danger'
            )
            return redirect(reverse_lazy(self.permission_denied_redirect_url))
        return super().dispatch(request, *args, **kwargs)
