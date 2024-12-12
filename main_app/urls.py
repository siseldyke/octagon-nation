from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('events/', views.event_index, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),
]