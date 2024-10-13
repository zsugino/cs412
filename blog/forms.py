from django import forms
from .models import Comment

class CreateCommentForm(forms.ModelForm):
  '''A form to add a Comment to the database'''

  class Meta:
    '''associate this form with the Comment Model; select fields.'''
    model = Comment
    fields = ['author', 'text',]