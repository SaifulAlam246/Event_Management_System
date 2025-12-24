from django.contrib import admin
from django.urls import path
from users.views import *


urlpatterns = [
    path('admin-dashboard/',admin_dashboard,name='admin-dashboard'),
    path('organizer-dashboard/',organizer_dashboard,name='organizer-dashboard'),
    path('participant-dashboard/',participant_dashboard,name='participant-dashboard'),

    path('sign-up/',sign_up,name='sign-up'),
    path('sign-in/',sign_in,name='sign-in'),
    path('sign-out/',sign_out,name='sign-out'),
    path('assign-role/<int:user_id>/',assign_role,name='assign-role'),
    path('create-group/',create_group,name='create-groups'),
    path('group-list/',group_list,name='group-list'),

    path('add-rsvp/<int:event_id>/',add_rsvp,name='add-rsvp'),
    path('view-rsvp-events/',view_rsvp_events,name='view-rsvp-events'),
    path('activate/<int:user_id>/<str:token>/',activate_user)
]