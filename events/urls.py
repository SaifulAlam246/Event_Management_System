from django.contrib import admin
from django.urls import path
from events.views import EventList,SearchEvents,EventDetail,EventCreate,EventUpdate,EventDelete, participant_list,participant_delete,category_list,category_create,category_update,category_delete

urlpatterns = [
    
   # path('view-dashboard/',view_dashboard,name='view_dashboard'),
   path('search-events/',SearchEvents.as_view(),name='search_events'),

   path('all-events/',EventList.as_view(),name='event_list'),
   path('events-detail/<int:id>/',EventDetail.as_view(),name='event_detail'),
   path('event-create/',EventCreate.as_view(),name='event_create'),
   path('event-update/<int:id>/',EventUpdate.as_view(),name='event_update'),
   path('event-delete/<int:id>/',EventDelete.as_view(),name='event_delete'),

   path('participants/',participant_list,name='participant_list'),
   # path('participant-create/',participant_create,name='participant_create'),
   # path('participant-update/<int:id>/',participant_update,name='participant_update'),
   path('participant-delete/<int:id>/',participant_delete,name='participant_delete'),

   path('category/',category_list,name='category_list'),
   path('category-create/',category_create,name='category_create'),
   path('category-update/<int:id>/',category_update,name='category_update'),
   path('category-delete/<int:id>/',category_delete,name='category_delete'),
]

