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

  def get_friends(self):
    '''Return list of friends profile'''
    friends1 = Friend.objects.filter(profile1=self)
    friends2 = Friend.objects.filter(profile2=self)

    all_my_friends = []

    for elem in friends1:
      all_my_friends.append(elem.profile2)

    for elem in friends2:
      all_my_friends.append(elem.profile1)

    return all_my_friends

  def add_friend(self, other):
    """ Add a friend relation between self and other """

    # mae sure no self friending
    if self == other:
      return

    check_frienship1 = Friend.objects.filter(profile1=self, profile2=other).exists()
    check_frienship2 = Friend.objects.filter(profile1=other, profile2=self).exists()

    # Not Friends Yet
    if not check_frienship1 and not check_frienship2:
      Friend.objects.create(profile1=self, profile2=other)

  def get_friend_suggestions(self):
    """ Return list of possible friends for a profile """
    suggestion_profiles = []
    my_friends = self.get_friends()
    all_profiles = Profile.objects.exclude(pk=self.pk)

    for user in all_profiles:
      if  user not in my_friends:
        suggestion_profiles.append(user)

    return suggestion_profiles

  def get_news_feed(self):
    """ Return a list of all statusmessage for a profile"""
    me_and_friends = [self] + list(self.get_friends()) 
    news_feed = StatusMessage.objects.filter(profile__in=me_and_friends).order_by('-timestamp')
    return news_feed


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


class Friend(models.Model):
  """Encapsulate the idea of an edge connecting two nodes with the app"""

  # data attributes of the Friends model
  profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1")
  profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2")

  timestamp = models.DateTimeField(auto_now=True)

  def __str__(self):
    """Returns a string representation of this Friends object"""
    return f'{self.profile1} & {self.profile2}'






