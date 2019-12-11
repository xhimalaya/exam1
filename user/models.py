from django.db import models

# Create your models here.
class Team(models.Model):
    identifier=models.CharField(primary_key=True,max_length=50, unique=True)
    name=models.CharField(max_length=100,blank=True)
    club_state=models.CharField(max_length=100,blank=True)
    logoUri=models.ImageField(upload_to="teamlogo/")

    def __str__(self):
        return self.identifier
class Player(models.Model):
    identifier=models.ForeignKey(Team,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=100,blank=False)
    lastName=models.CharField(max_length=100,blank=True)
    player_jersey_number=models.IntegerField()
    country=models.CharField(max_length=100,blank=False)
    imageUri=models.ImageField(upload_to="player_picture/")
    
class Player_history(models.Model):
    identifire=models.ForeignKey(Team,on_delete=models.CASCADE)
    matches=models.IntegerField()
    run=models.IntegerField()
    highest_scores=models.IntegerField()
    fifties=models.IntegerField()
    hundreds=models.IntegerField()
    
class Match(models.Model):
    team1=models.CharField(max_length=100,blank=True)
    team2=models.CharField(max_length=100,blank=True)
    winner=models.CharField(max_length=100,blank=True)
class Points(models.Model):
    team_name=models.CharField(max_length=100,blank=True)
    point=models.IntegerField()
