from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
  '''
  Store the data of one NBA player.
  PlayerID, First Name, Last Name, Position, Height, Weight, Birthday, 
  Country, School, Draft Year, Draft Round, Draft Number
  '''

  # identification
  player_id = models.IntegerField()
  first_name = models.TextField()
  last_name = models.TextField()
  birthday = models.DateField()
  country = models.TextField()
  school = models.TextField()
  position = models.TextField()
  height = models.TextField()
  weight = models.IntegerField()
  draft_year = models.IntegerField()

  def __str__(self):
    '''Returns a string representation of this model instance'''
    return f'{self.first_name} {self.last_name}'

class Ranking(models.Model):
  '''Store data of ranking created by user'''
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  position = models.TextField()
  rank = models.IntegerField()

  def __str__(self):
    '''Returns a string representation of this model instance'''
    return f'User: {self.user.username}, Position: {self.position}, Name: {self.player}, Rank: {self.rank}'

class DreamTeam(models.Model):
  '''Store data of dream team that user creates'''
  name = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  point_guard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dream_point_guard')
  shooting_guard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dream_shooting_guard')
  small_forward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dream_small_forward')
  power_forward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dream_power_forward')
  center = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='dream_center')
  created_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    '''Returns a string representation of this model instance'''
    return f'Dream Team: {self.name} created by {self.user.username}'

class Review(models.Model):
  '''Store data of review of the dreamteam by a user'''
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  dream_team = models.ForeignKey(DreamTeam, on_delete=models.CASCADE)
  content = models.TextField()
  created_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    '''Returns a string representation of this model instance'''
    return f'{self.user.username} Reviewing: {self.dream_team}'

class PlayerReview(models.Model):
  '''Store data of review for individual NBA players'''
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  content = models.TextField()
  rating = models.IntegerField()
  created_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    '''Returns a string representation of this model instance'''
    return f'{self.user.username} Reviewing: {self.player}'

def load_data():
  '''Function to load data records from CSV file into Django model instances'''
  # delete existing records to prevent duplicates:
  Player.objects.all().delete()

  filename = '/Users/xysugino/Desktop/players.csv'
  f = open(filename)
  f.readline() # discard headers

  for line in f:
    fields = line.split(',')

    try:
      # create a new instance of Player object with this record from CSV
      player = Player(player_id=fields[0],
                      first_name=fields[1],
                      last_name=fields[2],
                      position=fields[3],
                      height=fields[4],
                      weight=fields[5],
                      birthday=fields[6],
                      country=fields[7],
                      school=fields[8],
                      draft_year=fields[9],
      )

      player.save() # commit to database
      print(f'Created result: {player}')
      
    except Exception as e:
      print(f'Skipped: {fields}')
      
  print(f'Done. Created {len(Player.objects.all())} Players.')







  




