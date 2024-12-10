# File: views.py
# Author: Zai Sugino (xysugino@bu.edu), 12/10/2024
# Description: Various Class View to handle view functions

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Player, DreamTeam, Ranking, Review, PlayerReview
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateDreamTeamForm, UpdateDreamTeamForm, CreateReviewForm, CreateRankingForm, CreatePlayerReviewForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login # NEW
from django.shortcuts import redirect

# Create your views here.

class PlayersListView(ListView):
  '''View to display all NBA players'''

  template_name = 'nba/players.html'
  model = Player
  context_object_name = 'players'

  def get_queryset(self):
    '''Overrides default query set and produces custom order'''

    # display default view by order of draft year
    qs = super().get_queryset().order_by('draft_year')

    # filter result based on these fields
    if 'first_name' in self.request.GET:
      first_name = self.request.GET['first_name']
      if first_name:
        qs = qs.filter(first_name=first_name)

    if 'draft_year' in self.request.GET:
      draft_year = self.request.GET['draft_year']
      if draft_year:
        qs = qs.filter(draft_year=draft_year)

    if 'position' in self.request.GET:
      position = self.request.GET['position']
      if position:
        qs = qs.filter(position=position)

    if 'height' in self.request.GET:
      height = self.request.GET['height']
      if height:
        qs = qs.filter(height=height)

    return qs

class PlayerDetailView(DetailView):
  '''View to display single NBA player'''

  template_name='nba/player.html'
  model = Player
  context_object_name = 'player'

  def get_context_data(self, **kwargs):
    '''Override context to add more data to context object'''
    context = super().get_context_data(**kwargs)
    context['reviews'] = PlayerReview.objects.filter(player=self.object)
    return context
    
class DreamTeamListView(ListView):
  '''View to display all the dream team created by user'''

  template_name='nba/dream_teams.html'
  model = DreamTeam
  context_object_name = 'dream_teams'

  def get_queryset(self):
    '''Displayes only dream teams of the current user'''
    return DreamTeam.objects.filter(user=self.request.user)

class DreamTeamDetailView(DetailView):
  '''View to display one specific dream team by user'''

  template_name = 'nba/dream_team.html'
  model = DreamTeam
  context_object_name = 'dream_team'

  def get_context_data(self, **kwargs):
    '''Override context to add more data to context object'''
    context = super().get_context_data(**kwargs)
    context['reviews'] = Review.objects.filter(dream_team=self.object)
    return context

class RankingListView(LoginRequiredMixin, ListView):
  '''View to display the ranking by each position that the user created'''
  template_name = 'nba/rankings.html'
  model = Ranking
  context_object_name = 'rankings'

  def get_queryset(self):
    return Ranking.objects.filter(user=self.request.user).order_by('position', 'rank')

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class CreateDreamTeamView(LoginRequiredMixin, CreateView):
  '''View to create a new dreamteam and save it to the database'''
  form_class = CreateDreamTeamForm
  template_name = "nba/create_team_form.html"

  def form_valid(self, form):
    '''Handle form submission to create new dream team'''
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('dream_team_detail', kwargs={'pk': self.object.pk})

class UpdateDreamTeamView(LoginRequiredMixin, UpdateView):
  '''A view to update a dreamteam and save it to the database'''
  form_class = UpdateDreamTeamForm
  template_name = "nba/update_team_form.html"
  model = DreamTeam
  context_object_name = "dream_team"

  def form_valid(self, form):
    '''Handle form submission to update new dream team'''
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('dream_team_detail', kwargs={'pk': self.object.pk})

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class DeleteDreamTeamView(LoginRequiredMixin, DeleteView):
  """A view to delete a dreamteam and reflect it on to the database"""
  model = DreamTeam
  template_name = "nba/delete_team_form.html"
  context_object_name = "dream_team"

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully deleteing dreamteam.'''
    return reverse('dream_team_list')

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class PublicDreamTeamListView(LoginRequiredMixin, ListView):
  '''A view to display all the dream team'''
  template_name = 'nba/public_dream_teams.html'
  model = DreamTeam
  context_object_name = 'dream_teams'

  def get_queryset(self):
    '''Show all dreamteams created by other users exlcluding the onese you created'''
    return DreamTeam.objects.exclude(user=self.request.user)

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')

class CreateReviewView(LoginRequiredMixin, CreateView):
  '''A view to enable user to create review for other users dreamteam'''
  form_class = CreateReviewForm
  template_name = "nba/create_review_form.html"
  model = Review

  def form_valid(self, form):
    '''Handle form submission to create new review'''
    dream_team = DreamTeam.objects.get(pk=self.kwargs['pk'])
    form.instance.user = self.request.user
    form.instance.dream_team = dream_team
    self.dt_pk = dream_team.pk
    return super().form_valid(form)

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('dream_team_detail', kwargs={'pk': self.dt_pk})

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')


class CreateRankingView(LoginRequiredMixin, CreateView):
  '''A view to enable user to create ranking for NBA Players'''
  form_class = CreateRankingForm
  template_name = 'nba/create_ranking_form.html'

  def form_valid(self, form):
    '''Handle form submission to create new ranking'''
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('ranking_list')

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')


class CreateReviewPlayerView(LoginRequiredMixin, CreateView):
  '''A view to enable user to create review for individual NBA players'''
  form_class = CreatePlayerReviewForm
  template_name = 'nba/create_review_player_form.html'

  def form_valid(self, form):
    '''Handle form submission to create new player review'''
    player = Player.objects.get(pk=self.kwargs['pk'])
    form.instance.user = self.request.user
    form.instance.player = player
    return super().form_valid(form)

  def get_success_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('player_detail', kwargs={'pk': self.kwargs['pk']})

  def get_login_url(self) -> str:
    '''return the URL required for login'''
    return reverse('login')


class RegistrationView(CreateView):
    '''
    show/process form for account registration
    '''
    template_name = 'nba/register.html'
    form_class = UserCreationForm
    def dispatch(self, *args, **kwargs):
        '''
        Handle the User creation part of the form submission, 
        '''
        # handle the POST:
        if self.request.POST:
            # reconstruct the UserCreationForm from the POST data
            user_form = UserCreationForm(self.request.POST)
            # create the user and login
            user = user_form.save()     
            print(f"RegistrationView.form_valid(): Created user= {user}")   
            login(self.request, user)
            print(f"RegistrationView.form_valid(): User is logged in")   
            
            return redirect(reverse('home'))
        
        # GET: handled by super class
        return super().dispatch(*args, **kwargs)






  

  











  


  




  







  

