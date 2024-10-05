# File: urls.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Matches the url pattern with the correct view

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
  path('', views.ShowAllView.as_view(), name='show_all_profiles'),
]