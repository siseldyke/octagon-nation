from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_index, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),

]