# File: urls.py
# Author: Zai Sugino (xysugino@bu.edu), 12/10/2024
# Description: Various url routes to handle routing path

from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

# map URL to each view
urlpatterns = [
    path(r'', views.PlayersListView.as_view(), name='home'),
    path(r'players', views.PlayersListView.as_view(), name='players_list'),
    path(r'player/<int:pk>', views.PlayerDetailView.as_view(), name='player_detail'),
    path(r'player/<int:pk>/review/', views.CreateReviewPlayerView.as_view(), name='create_player_review'),
    path(r'public_dream_teams', views.PublicDreamTeamListView.as_view(), name='public_dream_team_list'),
    path(r'dream_teams', views.DreamTeamListView.as_view(), name='dream_team_list'),
    path(r'dream_team/<int:pk>', views.DreamTeamDetailView.as_view(), name='dream_team_detail'),
    path(r'dream_team/<int:pk>/update/', views.UpdateDreamTeamView.as_view(), name='update_dream_team'),
    path(r'dream_team/<int:pk>/delete/', views.DeleteDreamTeamView.as_view(), name='delete_dream_team'),
    path(r'dream_team/create_dream_team/', views.CreateDreamTeamView.as_view(), name='create_dream_team'),
    path(r'dream_team/<int:pk>/review/', views.CreateReviewView.as_view(), name='create_review'),
    path(r'rankings/', views.RankingListView.as_view(), name='ranking_list'),
    path(r'rankings/create/', views.CreateRankingView.as_view(), name='create_ranking'),
    path(r'login/', auth_views.LoginView.as_view(template_name='nba/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(next_page='players_list'), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]
