# File: views.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Contains the views classes and function that
# interact with model and delegate work to template

from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.
class ShowAllView(ListView):
  """Create a subclass of ListView to display all profile"""
  model = Profile
  template_name = "mini_fb/show_all_profiles.html"
  context_object_name = "profiles"


