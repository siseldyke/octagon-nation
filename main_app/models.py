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