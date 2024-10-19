# File: models.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: The data model for our mini_fb application

from django.db import models
from django.urls import reverse

class Profile(models.Model):
  """Encapsulate the attributes of 
  individual facebook users
  """

  # data attributes of the profile model
  first_name = models.TextField(blank=False)
  last_name = models.TextField(blank=False)
  city = models.TextField(blank=False)
  email = models.TextField(blank=False)
  image_url = models.URLField(blank=True)

  def __str__(self):
    """Return a string representation of Profile object"""
    return f'{self.first_name} {self.last_name}'
  
  def get_status_messages(self):
    """Return all the status message for this profile"""
    status_messages = StatusMessage.objects.filter(profile=self)
    return status_messages

  def get_absolute_url(self):
    '''Return the URL to this profile'''
    return reverse('show_profile', kwargs={'pk': self.pk})


class StatusMessage(models.Model):
  """Encapsulates the attributes of 
  status message for a user
  """

  # data attributes of the StatusMessage model
  profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now=True)
  message = models.TextField(blank=False)

  def __str__(self):
    '''Return a string representation of this StatusMessage object.'''
    return f'{self.message}'

  def get_images(self):
    """Return all the images for this status message"""
    images = Image.objects.filter(status_message=self)
    return images
  

class Image(models.Model):
  """Encapsulates the attributes of Image for a Status Message"""

  image_file = models.ImageField(blank=True)
  status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now=True)

  def __str__(self):
    '''Return a string representation of this Image object.'''
    return f'{self.timestamp}'





