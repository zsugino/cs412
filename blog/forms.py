from django import forms
from .models import Comment, Article

class CreateCommentForm(forms.ModelForm):
  '''A form to add a Comment to the database'''

  class Meta:
    '''associate this form with the Comment Model; select fields.'''
    model = Comment
    fields = ['author', 'text',]


class CreateArticleForm(forms.ModelForm):
    '''A form to add a new Article to the database.'''
    class Meta:
        '''Associate this form with the Article model; select fields to add.'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']
    ## other class(es)