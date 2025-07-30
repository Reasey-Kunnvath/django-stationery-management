
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('login/auth', views.auth_adm_login, name='auth_adm_login'),
]
