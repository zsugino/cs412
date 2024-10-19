# File: urls.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Matches the url pattern with the correct view

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
  path('', views.ShowAllView.as_view(), name='show_all_profiles'),
  path('profile/<int:pk>', views.ShowProfilePageView.as_view(), name='show_profile'),
  path('create_profile', views.CreateProfileView.as_view(), name='create_profile'),
  path('profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name='create_status'), 
  path('profile/<int:pk>/update', views.UpdateProfileView.as_view(), name='update_profile'),
  path('status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name='delete_status'),
  path('status/<int:pk>/update', views.UpdateStatusMessageView.as_view(), name='update_status'),

]

