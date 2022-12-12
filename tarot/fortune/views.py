from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Fortune


class FortuneListView(ListView):
    model = Fortune
    template_name = 'fortune/fortune_lists.html'
    context_object_name = 'fortune_list'

    def get_queryset(self):
        return Fortune.objects.all()

    def post(self, request, *args, **kwargs):
        pass


class FortuneDetailView(DetailView):
    model = Fortune
    template_name = 'fortune/fortune_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
