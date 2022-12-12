from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Fortune


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
    template_name = 'fortune/fortune_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
