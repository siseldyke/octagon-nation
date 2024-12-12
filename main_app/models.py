from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=255)   
    attendees = models.PositiveIntegerField()  
    location = models.CharField(max_length=255)  
    date = models.DateField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.location} ({self.date})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=255, blank=True, null=True)
    basic_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'