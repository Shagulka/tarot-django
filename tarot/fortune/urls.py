from django.urls import path

from . import views

app_name = 'fortune'
urlpatterns = [
    path('', views.FortuneListView.as_view(), name="fortune_list"),
    path(
        '<slug:slug>/',
        views.FortuneDetailView.as_view(),
        name='fortune_detail'
    ),
]
