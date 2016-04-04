
from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    '''
    Models someone who may vote
    '''
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Flag(models.Model):
    '''
    Models a flag which may be voted on
    '''
    name = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024)
            
    def __str__(self):
        return self.name


class Vote(models.Model):
    '''
    Models a single vote cast by a `Voter` for a `Flag`
    '''
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
