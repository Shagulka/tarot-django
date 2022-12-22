import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import BankAccount


class GetBonusMoneyView(LoginRequiredMixin, DetailView):
    model = BankAccount
    template_name = 'coins/get-bonus-money.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        return BankAccount.objects.get(user=self.request.user)

    def get(self, *args, **kwargs):
        """Page for getting bonus money

        if user already got bonus money in last 24 hours, then he can't get it again

        then redirect to previous page
        """
        self.object = self.get_object()
        last_bonus_time = self.object.bonus
        # last_bonus_time = pytz.timezone(self.object.timezone).localize(
        #     self.object.bonus).astimezone(pytz.timezone(settings.TIME_ZONE))
        if last_bonus_time:
            if datetime.datetime.now(
                    timezone.utc
            ) - last_bonus_time >= datetime.timedelta(hours=24):
                self.object.balance += 20

                self.object.bonus = datetime.datetime.now(timezone.utc)
                self.object.save()
        else:
            self.object.balance += 20

            self.object.bonus = datetime.datetime.now(timezone.utc)
            self.object.save()

        return redirect(self.request.META.get('HTTP_REFERER', '/'))
