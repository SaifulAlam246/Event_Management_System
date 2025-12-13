from django.contrib import admin
from django.urls import path
from events.views import *


urlpatterns = [
    
   path('view-dashboard/',view_dashboard,name='view_dashboard'),
   path('search-events/',search_events,name='search_events'),

   path('all-events/',event_list,name='event_list'),
   path('events-detail/<int:id>/',event_detail,name='event_detail'),
   path('event-create/',event_create,name='event_create'),
   path('event-update/<int:id>/',event_update,name='event_update'),
   path('event-delete/<int:id>/',event_delete,name='event_delete'),

   path('participants/',participant_list,name='participant_list'),
   path('participant-create/',participant_create,name='participant_create'),
   path('participant-update/<int:id>/',participant_update,name='participant_update'),
   path('participant-delete/<int:id>/',participant_delete,name='participant_delete'),

   path('category/',category_list,name='category_list'),
   path('category-create/',category_create,name='category_create'),
   path('category-update/<int:id>/',category_update,name='category_update'),
   path('category-delete/<int:id>/',category_delete,name='category_delete'),
]

