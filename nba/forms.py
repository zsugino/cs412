from django import forms
from .models import DreamTeam, Review

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