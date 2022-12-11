from django.views.generic import ListView


class FortuneListView(ListView):
    # model = Fortune
    template_name = 'fortune/fortune_lists.html'
    context_object_name = 'fortune_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        pass

    def post(self, request, *args, **kwargs):
        pass
