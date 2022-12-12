from django.urls import path

from . import views

app_name = 'fortune'
urlpatterns = [
    path('', views.FortuneListView.as_view(), name="fortune_list"),
    path('<int:pk>/', views.FortuneDetailView.as_view(), name='fortune_detail'),
]
