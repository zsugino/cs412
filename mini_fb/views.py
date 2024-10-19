# File: views.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Contains the views classes and function that
# interact with model and delegate work to template

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Image, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm, UpdateStatusMessageForm
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

    # save the status message to database
    sm = form.save()

    # read the file from the form:
    files = self.request.FILES.getlist('files')

    # create image object for each file
    for file in files:
      img = Image()
      img.status_message = sm
      img.image_file = file 
      img.save()
  
    return super().form_valid(form)
    
  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


class UpdateProfileView(UpdateView):
  """A view to update a profile and save it to the database"""
  form_class = UpdateProfileForm
  template_name = "mini_fb/update_profile_form.html"
  model = Profile
  context_object_name = "profile"

class DeleteStatusMessageView(DeleteView):
  """A view to delete a status message and reflect it on to the database"""
  model = StatusMessage
  template_name = "mini_fb/delete_status_form.html"
  context_object_name = "status"

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully deleteing status message.'''
    p_pk = self.object.profile.pk

    # reverse to show the article page
    return reverse('show_profile', kwargs={'pk': p_pk})

class UpdateStatusMessageView(UpdateView):
  """A view to update a status message and reflect it on to the database"""
  form_class = UpdateStatusMessageForm
  model = StatusMessage
  template_name = "mini_fb/update_status_form.html"
  context_object_name = "status"

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully updating status message.'''
    p_pk = self.object.profile.pk
    # reverse to show the article page
    return reverse('show_profile', kwargs={'pk': p_pk})














