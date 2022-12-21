from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import redirect
from django.urls import reverse_lazy


class StuffPermissionRequiredMixin(PermissionRequiredMixin):
    permission_denied_message = 'У вас нет доступа к этой странице'
    permission_denied_redirect_url = 'homepage:home'
    permission_required = ('user.is_staff',)

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message,
                       extra_tags='danger')
        return redirect(reverse_lazy(self.permission_denied_redirect_url))


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
