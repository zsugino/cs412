# File: forms.py
# Author: Zai Sugino (xysugino@bu.edu), 12/10/2024
# Description: Various Forms to handle form submission

from django import forms
from .models import DreamTeam, Review, Ranking, PlayerReview

class CreateDreamTeamForm(forms.ModelForm):
  '''A form to add a new dreamteam to the database'''

  class Meta:
    '''Associates this form with the DreamTeam Model'''
    model = DreamTeam
    fields = ['name', 'point_guard', 'shooting_guard', 'small_forward', 'power_forward', 'center']


class UpdateDreamTeamForm(forms.ModelForm):
  '''A form to update existing dreamteam to the database'''

  class Meta:
    '''Associates this form with the DreamTeam Model'''
    model = DreamTeam
    fields = ['name', 'point_guard', 'shooting_guard', 'small_forward', 'power_forward', 'center']


class CreateReviewForm(forms.ModelForm):
  '''A form to create a new review of a dreamteam to the database'''

  class Meta:
    model = Review
    fields = ['content']

class CreateRankingForm(forms.ModelForm):
  '''A form to create a new ranking for a user'''

  class Meta:
    model = Ranking
    fields = ['player', 'position', 'rank']

class CreatePlayerReviewForm(forms.ModelForm):
  '''A form to create a review for a individual player by a user'''

  class Meta:
    model = PlayerReview
    fields = ['content', 'rating']
    













