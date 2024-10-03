# File: models.py
# Author: Zai Sugino (xysugino@bu.edu), 10/03/2024
# Description: The data model for our mini_fb application

from django.db import models

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

