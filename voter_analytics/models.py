from django.db import models

# Create your models here.

class Voter(models.Model):
  """Stores voter data"""
  
  # Identification
  voter_id_number = models.TextField()
  first_name = models.TextField()
  last_name = models.TextField()
  date_of_birth = models.DateField()
  date_of_registration = models.DateField()
  party_affiliation = models.TextField()
  precinct_number = models.TextField()

  # Resedential Address
  ra_street_number = models.TextField()
  ra_street_name = models.TextField()
  ra_apartment_number = models.TextField()
  ra_zip_code = models.TextField()

  # Participation
  v20state = models.BooleanField(default=False)
  v21town = models.BooleanField(default=False)
  v21primary = models.BooleanField(default=False)
  v22general = models.BooleanField(default=False)
  v23town = models.BooleanField(default=False)

  voter_score = models.IntegerField()

  def __str__(self):
    '''Return a string representation of this model instance.'''
    return f'{self.first_name} {self.party_affiliation}'


def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
    # delete existing records to prevent duplicates:
    Voter.objects.all().delete()
    
    filename = '/Users/xysugino/Desktop/newton_voters.csv'
    f = open(filename)
    f.readline() # discard headers

    for line in f:
        fields = line.split(',')

        v20state = fields[11].strip() == "TRUE"
        v21town = fields[12].strip() == "TRUE"
        v21primary = fields[13].strip() == "TRUE"
        v22general = fields[14].strip() == "TRUE"
        v23town = fields[15].strip() == "TRUE"
       
        try:
            # create a new instance of Result object with this record from CSV
            voter = Voter(voter_id_number=fields[0],
                            last_name=fields[1],
                            first_name=fields[2],
                            ra_street_number = fields[3],
                            ra_street_name = fields[4],
                            ra_apartment_number = fields[5],
                            ra_zip_code = fields[6],
                            date_of_birth = fields[7],
                            date_of_registration = fields[8],
                            party_affiliation = fields[9].strip(),
                            precinct_number = fields[10],
                            v20state =  v20state,
                            v21town = v21town,
                            v21primary = v21primary,
                            v22general = v22general,
                            v23town = v23town,
                            voter_score = fields[16],
                        )
        
            voter.save() # commit to database
            print(f'Created result: {voter}')
            
        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Voter.objects.all())} Voters.')

