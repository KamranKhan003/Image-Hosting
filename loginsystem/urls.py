from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('profile/', views.profile, name='profile'),


    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),

    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]