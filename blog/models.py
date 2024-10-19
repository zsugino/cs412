from django.db import models
from django.urls import reverse

# Create your models here.

# Define data models for use in blog application
class Article(models.Model):
  '''Encapsulate the idea of an Article by some author'''

  # data attributes of a Article
  title = models.TextField(blank=False)
  author = models.TextField(blank=False)
  text = models.TextField(blank=False)
  published = models.DateTimeField(auto_now=True)
  # image_url = models.URLField(blank=True)
  image_file = models.ImageField(blank=True)

  def __str__(self):
    '''Return a string representation of this Article object'''
    return f'{self.title} by {self.author}'

  def get_comments(self):
    '''Return all of the comments about this article'''
    comments = Comment.objects.filter(article=self)
    return comments

  def get_absolute_url(self):
    '''Return the URL to display this Article.'''
    return reverse('article', kwargs={'pk':self.pk})


class Comment(models.Model):
  '''Encapsulate the idea of a Comment on an Article.'''

  # data attributes of a Comment:
  article = models.ForeignKey("Article", on_delete=models.CASCADE)
  author = models.TextField(blank=False)
  text = models.TextField(blank=False)
  published = models.DateTimeField(auto_now=True)
    
  def __str__(self):
    '''Return a string representation of this Comment object.'''
    return f'{self.text}'




