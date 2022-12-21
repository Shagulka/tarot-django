from django.urls import path

from . import views

app_name = 'coins'
urlpatterns = [
    path(
        'get-bonus-money/',
        views.GetBonusMoneyView.as_view(),
        name='get_bonus_money'
    )
]
