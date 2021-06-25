from django.urls import path
from django.contrib.auth import views as auth_view
from .views import Register, Profile, ProfileUpdate


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile'),
    path('update_profile/', ProfileUpdate.as_view(), name='update_profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
         template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
         template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
         template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
         template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
