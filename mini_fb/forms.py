from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
  """A form to add a new profile to the database"""

  class Meta:
    """Associates this form with the Profile Model"""
    model = Profile
    fields = ['first_name', 'last_name', 'city', 'email', 'image_url',]


class CreateStatusMessageForm(forms.ModelForm):
  """A form to add a new message status to the database"""

  class Meta:
    """Associates this form with the Status Message Model"""
    model = StatusMessage
    fields = ['message',]