import datetime

from coins.models import BankAccount


def add_user_balance_to_context(request):
    """Add user balance and bonus money wait time
    to context for all pages if user is authenticated
    """
    if request.user.is_authenticated:
        context = {}
        balance = BankAccount.objects.get(user=request.user.id).balance
        context['balance'] = balance
        bonus_time = BankAccount.objects.get(user=request.user.id).bonus
        if bonus_time:
            if datetime.datetime.now(
                    datetime.timezone.utc
            ) - bonus_time >= datetime.timedelta(hours=24):
                context['bonus_status'] = 'Получить сейчас!'
            else:
                time_left = datetime.timedelta(hours=24) - (
                    datetime.datetime.now(datetime.timezone.utc) - bonus_time
                )
                context['bonus_status'] = (
                    f'Осталось {time_left.seconds // 3600}:'
                    f'{time_left.seconds % 3600 // 60}'
                )

        else:
            context['bonus_status'] = 'Получить сейчас!'
        return context
    return {}
