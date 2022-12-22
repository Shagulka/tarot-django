import datetime
import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from coins.models import BankAccount
from deck.generators import Deck

from .models import Fortune


class FortuneListView(LoginRequiredMixin, ListView):
    model = Fortune
    template_name = 'fortune/fortune_lists.html'
    context_object_name = 'fortune_list'

    # def get_queryset(self):
    # return Fortune.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fortunes'] = self.get_queryset()
        return context


class FortuneDetailView(LoginRequiredMixin, DetailView):
    model = Fortune

    def get_template_names(self):
        if self.object.type_fortune_telling == 1:
            return 'fortune/tarot/tarot_1.html'
        elif self.object.type_fortune_telling == 2:
            return 'fortune/tarot/tarot_2.html'
        elif self.object.type_fortune_telling == 3:
            return 'fortune/tarot/tarot_3.html'
        elif self.object.type_fortune_telling == 4:
            return 'fortune/tarot/tarot_4.html'
        elif self.object.type_fortune_telling == 5:
            return 'fortune/tarot/tarot_2_3.html'
        elif self.object.type_fortune_telling == 6:
            return 'fortune/tarot/tarot_3_3.html'
        elif self.object.type_fortune_telling == 7:
            return 'fortune/tarot/tarot_H.html'
        elif self.object.type_fortune_telling == 8:
            return 'fortune/tarot/tarot_star.html'
        elif self.object.type_fortune_telling == 9:
            return 'fortune/tarot/tarot_9.html'

    def get_context_data(self, **kwargs):
        cards, prediction = Deck().get_cards(self.object, self.request.user)
        context = super().get_context_data(**kwargs)
        context['cards'] = cards
        context['prediction'] = prediction
        context['fortune'] = self.get_object()
        return context

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(object=self.object)
        bank_account = get_object_or_404(BankAccount, user=self.request.user)

        if self.object.price <= bank_account.balance:

            if (self.request.user.date_of_birth is not None and
                    self.request.user.first_name is not None and
                    self.request.user.last_name is not None):

                bank_account.balance -= self.object.price
                bank_account.save()
                logger = logging.getLogger('django')
                fh = logging.FileHandler('fortune.log')
                logger.addHandler(fh)
                logger.info(f'Пользователь {self.request.user}'
                            f' оплатил гадание {self.object.name}'
                            f' за {self.object.price} монет'
                            f' в {datetime.datetime.now()}')
            else:
                messages.error(
                    self.request,
                    'Гадания недоступны,'
                    ' так как вы не заполнили обязательные данные профиля'
                )
                return redirect('fortune:fortune_list')
        else:
            messages.error(self.request, 'Недостаточно средств')
            return redirect('fortune:fortune_list')

        return super().get(*args, **kwargs)
