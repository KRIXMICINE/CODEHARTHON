from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length= 200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200) # This creates a new topic
    
    def __str__(self):
        return self.name


class Room(models.Model): # This is the parent table in the dtabase. Then the attributes comes under.
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # models.SET_NULL allows you to delete the topic without deleting the room. You must allow null=true in the database.
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering =['-updated', '-created']
      
    def __str__(self):
        return self.name
   
   
class Message(models.Model): # This allows the user to create a message
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering =['-updated', '-created']
    
    
    def __str__(self):
        return self.body[0:50]

