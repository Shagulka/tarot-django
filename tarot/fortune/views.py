from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from coins.models import BankAccount
from deck.generators import Deck
from users.permissions import CustomLoginRequiredMixin

from .models import Fortune


class FortuneListView(LoginRequiredMixin, ListView):
    model = Fortune
    template_name = 'fortune/fortune_lists.html'
    context_object_name = 'fortune_list'

    def get_queryset(self):
        return Fortune.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fortunes'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FortuneDetailView(CustomLoginRequiredMixin, DetailView):
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
        bank_account = get_object_or_404(BankAccount, user=self.request.user)
        if self.object.price <= bank_account.balance:
            bank_account.balance -= self.object.price
            bank_account.save()
        else:
            self.object = None
            messages.error(self.request, 'Недостаточно средств')
            return redirect('fortune:fortune_list')
        cards, prediction = Deck().get_cards(self.object)
        context = super().get_context_data(**kwargs)
        context['cards'] = cards
        context['prediction'] = prediction
        context['fortune'] = self.object
        return context
