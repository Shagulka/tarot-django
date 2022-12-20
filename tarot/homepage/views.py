from django.shortcuts import redirect, render
from django.urls import reverse


def home(request):
    template_name = 'homepage/homepage.html'
    if request.user.is_authenticated:
        return redirect(reverse('fortune:fortune_list'))
    return render(request, template_name)
