import datetime

from django.contrib import messages
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

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(object=self.object)
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
                messages.error(
                    self.request,
                    'Получить бонусные монетки можно только раз в 24 часа'
                )

                return redirect('fortune:fortune_list')
        else:
            self.object.balance += 20

            self.object.bonus = datetime.datetime.now(timezone.utc)
            self.object.save()

        return super().get(*args, **kwargs)
