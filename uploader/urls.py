from typing import MappingView
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('loginsystem.urls')),
    path('signup/', views.Signupview.as_view(), name='signup'),
    path('user_setting/<int:id>/', views.user_setting, name='user_setting'),
]
