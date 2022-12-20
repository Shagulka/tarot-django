from django.shortcuts import render

from coins.models import BankAccount


def home(request):
    template_name = 'homepage/homepage.html'
    context = {
    }
    if request.user.is_authenticated:
        balance = BankAccount.objects.get(user=request.user.id).balance
        context['balance'] = balance

    return render(request, template_name, context)
