from coins.models import BankAccount


def add_user_balance_to_context(request):
    if request.user.is_authenticated:
        balance = BankAccount.objects.get(user=request.user.id).balance
        return {'balance': balance}
    return {}
