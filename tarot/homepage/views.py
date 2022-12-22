from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    """Homepage view
    if user is authenticated, then redirect to fortune list page"""
    def dispatch(self, *args, **kwargs):
        template_name = 'homepage/homepage.html'
        if self.request.user.is_authenticated:
            return redirect(reverse('fortune:fortune_list'))

        return render(self.request, template_name)
