from django.urls import path

from fortune.views import FortuneListView

app_name = 'fortune'
urlpatterns = [
    path('', FortuneListView.as_view(), name="fortune_list")
]
