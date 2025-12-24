from django.contrib import admin
from django.urls import path
from core.views import *
from users.views import dashboard


urlpatterns = [
    path('dashboard/',dashboard,name='role-dashboard'),
    path('home/',home,name='home'),
    path('no-permission/',no_permission,name='no-permission')
]