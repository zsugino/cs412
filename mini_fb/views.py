# File: views.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: Contains the views classes and function that
# interact with model and delegate work to template

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Profile, Image, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm, UpdateStatusMessageForm
from typing import Any, Dict
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


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

class CreateProfileView(LoginRequiredMixin, CreateView):
  """A view to create a new profile and save it to the database"""
  form_class = CreateProfileForm
  template_name = "mini_fb/create_profile_form.html"

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

  def get_context_data(self, **kwargs: Any):
    """Build the dict for context data for this view"""
    context = super().get_context_data(**kwargs)
    context['user_form'] = UserCreationForm()
    return context

  def form_valid(self, form):
    """Handle form submission by reconstructing UserCreationForm"""
    reconstructed = UserCreationForm(self.request.POST)

    newUserInstance = reconstructed.save()

    form.instance.user = newUserInstance

    return super().form_valid(form)

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
  """A view to create a new status message and save it to the database"""
  form_class = CreateStatusMessageForm
  template_name = "mini_fb/create_status_form.html"

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    """Build the dict for context data for this view"""
    # superclass context data
    context = super().get_context_data(**kwargs)
    # find the corresponding profile
    profile = Profile.objects.get(user = self.request.user)
    # add profile to context data
    context['profile'] = profile
    return context
  
  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

  def form_valid(self, form):
    """Handle form submission by attatching profile to the status message object"""
    print(form.cleaned_data)
    # profile = Profile.objects.get(pk=self.kwargs['pk'])
    profile = Profile.objects.get(user = self.request.user)

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
    profile = Profile.objects.get(user = self.request.user)
    return reverse('show_profile', kwargs={'pk': profile.pk})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
  """A view to update a profile and save it to the database"""
  form_class = UpdateProfileForm
  template_name = "mini_fb/update_profile_form.html"
  model = Profile
  context_object_name = "profile"

  def get_object(self):
    '''return corresponsing profile'''
    return Profile.objects.get(user = self.request.user)

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
  """A view to delete a status message and reflect it on to the database"""
  model = StatusMessage
  template_name = "mini_fb/delete_status_form.html"
  context_object_name = "status"

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully deleteing status message.'''
    p_pk = self.object.profile.pk

    # reverse to show the article page
    return reverse('show_profile', kwargs={'pk': p_pk})

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
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

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')


class CreateFriendView(LoginRequiredMixin, View):
  def dispatch(self, request, *args, **kwargs):
    profile = Profile.objects.get(user = self.request.user)
    other = Profile.objects.get(pk=kwargs['other_pk'])
    profile.add_friend(other)
    return redirect('show_profile', pk=profile.pk)

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')


class ShowFriendSuggestionsView(DetailView):
  """Displays suggestion for a profile"""
  model = Profile
  template_name = "mini_fb/friend_suggestions.html"
  context_object_name = "profile"

  def get_object(self):
    '''return corresponsing profile'''
    return Profile.objects.get(user = self.request.user)


class ShowNewsFeedView(DetailView):
  """Displays newsfeed for a profile"""
  model = Profile
  template_name = "mini_fb/news_feed.html"
  context_object_name = "profile"

  def get_object(self):
    '''return corresponsing profile'''
    return Profile.objects.get(user = self.request.user)

















