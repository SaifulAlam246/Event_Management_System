from django.contrib import admin
from django.urls import path
from core.views import *
from users.views import dashboard


urlpatterns = [
    path('',home,name='home'),
    path('dashboard/',dashboard,name='role-dashboard'),
    path('no-permission/',no_permission,name='no-permission')
]