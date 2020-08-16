# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=100)
    singer = models.CharField(null=True,max_length=200)
    tag  = models.CharField(null=True,max_length=100)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='images')

    def __str__(self):
        return self.name

class Listenlater(models.Model):
    listen_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    music = models.CharField(null=True,max_length=100)

    def __str__(self):
        return self.user.username

