from django.db import models
from multiselectfield.db.fields import MultiSelectField

CATEGORY_CHOICES = [    ('WK', 'WK'),    ('BAT', 'BAT'),    ('AR', 'AR'),    ('BOWL', 'BOWL'),]
PLAYER_TYPE_CHOICES = [
        ('RH_BAT', 'Right-handed batsman'),
        ('LH_BAT', 'Left-handed batsman'),
        ('RF_FAST', 'Right-arm fast bowler'),
        ('LF_FAST', 'Left-arm fast bowler'),
        ('RF_MEDIUM_FAST', 'Right-arm medium-fast bowler'),
        ('LF_MEDIUM_FAST', 'Left-arm medium-fast bowler'),
        ('RF_MEDIUM', 'Right-arm medium bowler'),
        ('LF_MEDIUM', 'Left-arm medium bowler'),
        ('RF_OFFSPIN', 'Right-arm off-spin bowler'),
        ('LF_ORTHODOX', 'Left-arm orthodox spin bowler'),
        ('RF_LEGSPIN', 'Right-arm leg-spin bowler'),
        ('LF_UNORTHODOX', 'Left-arm unorthodox spin bowler'),
        ('RH_BAT_RF_FAST', 'Right-handed batsman and right-arm fast bowler'),
        ('LH_BAT_LF_FAST', 'Left-handed batsman and left-arm fast bowler'),
        ('RH_BAT_RF_OFFSPIN', 'Right-handed batsman and right-arm off-spin bowler'),
        ('LH_BAT_LF_ORTHODOX', 'Left-handed batsman and left-arm orthodox spin bowler'),
        ('RH_BAT_RF_LEGSPIN', 'Right-handed batsman and right-arm leg-spin bowler'),
        ('LH_BAT_LF_UNORTHODOX', 'Left-handed batsman and left-arm unorthodox spin bowler'),
        ('RH_WK', 'Right-handed wicketkeeper-batsman'),
        ('LH_WK', 'Left-handed wicketkeeper-batsman'),
    ]

UPCOMING = 'UP'
LIVE = 'LI'
COMPLETED = 'CO'

MATCH_STATUS_CHOICES = (
        (UPCOMING, 'Upcoming'),
        (LIVE, 'Live'),
        (COMPLETED, 'Completed'),
    )





class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    balance = models.FloatField(default=0.0)
    winnings = models.FloatField(default=0.00)

class Player(models.Model):
    name = models.CharField(max_length=255)
    points = models.FloatField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    player_type = MultiSelectField(choices=PLAYER_TYPE_CHOICES, max_choices=2,max_length=20,null=True)

class Match(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    players = models.ManyToManyField(Player, related_name='players')
    participants = models.ForeignKey('Participants', on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(max_length=2, choices=MATCH_STATUS_CHOICES, default=UPCOMING)


class Participants(models.Model):
    p1=models.CharField(max_length=25,null=True)
    p2=models.CharField(max_length=25,null=True)
    p1_logo = models.FileField(upload_to="static/media/logo", max_length=254)
    p2_logo = models.FileField(upload_to="static/media/logo", max_length=254)
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    players = models.ManyToManyField(Player, related_name='teams')
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    Contest = models.ForeignKey('Contest', on_delete=models.CASCADE, default=None)

class Contest(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=255)
    entry_fee = models.FloatField()
    prize_pool = models.FloatField()
    max_teams = models.IntegerField()
    teams_per_user = models.IntegerField(default=1)
    
class Sports(models.Model):
    name=models.CharField(max_length=15)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)