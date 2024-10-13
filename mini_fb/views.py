# File: views.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Contains the views classes and function that
# interact with model and delegate work to template

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from .forms import CreateProfileForm, CreateStatusMessageForm
from typing import Any, Dict
from django.urls import reverse

class ShowAllView(ListView):
  """Create a subclass of ListView to display all profile"""
  model = Profile
  template_name = "mini_fb/show_all_profiles.html"
  context_object_name = "profiles"

class ShowProfilePageView(DetailView):
  """Displays one profile"""
  model = Profile
  template_name = "mini_fb/show_profile.html"
  context_object_name = "profile"

class CreateProfileView(CreateView):
  """A view to create a new profile and save it to the database"""
  form_class = CreateProfileForm
  template_name = "mini_fb/create_profile_form.html"

class CreateStatusMessageView(CreateView):
  """A view to create a new status message and save it to the database"""
  form_class = CreateStatusMessageForm
  template_name = "mini_fb/create_status_form.html"

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    """Build the dict for context data for this view"""
    # superclass context data
    context = super().get_context_data(**kwargs)
    # find the pk from the URL
    pk = self.kwargs['pk']
    # find the corresponding profile
    profile = Profile.objects.get(pk=pk)
    # add profile to context data
    context['profile'] = profile
    return context

  def form_valid(self, form):
    """Handle form submission by attatching profile to the status message object"""
    print(form.cleaned_data)
    profile = Profile.objects.get(pk=self.kwargs['pk'])
    form.instance.profile = profile
    return super().form_valid(form)
    
  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})





