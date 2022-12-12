from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Fortune
from deck.generators import Deck

class FortuneListView(ListView):
    model = Fortune
    template_name = 'fortune/fortune_lists.html'
    context_object_name = 'fortune_list'

    def get_queryset(self):
        return Fortune.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fortunes'] =  self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class FortuneDetailView(DetailView):
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
        cards = Deck().get_cards(self.object)
        context = super().get_context_data(**kwargs)
        context['cards'] = cards
        context['fortune'] = self.object
        return context
