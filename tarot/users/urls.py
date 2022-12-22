from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='users/login.html',
             redirect_authenticated_user=True
         ),
         name='login'),
    path('logout/',
         views.CustomLogoutView.as_view(),
         name='logout'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='users/password_change.html',
             success_url='done/',
         ), name='password_change'),
    path('change-password/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='users/change_password_done.html'),
         name='password_change_done'),
    path('reset-password/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             email_template_name='users/password_reset_html_email.html',
             success_url='done/',
         ),
         name='password_reset'),
    path('reset-password/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/reset_password_complete.html'),
         name='password_reset_complete'),

    path('signup/', views.SignUpFormView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdate.as_view(), name='profile'),
]
