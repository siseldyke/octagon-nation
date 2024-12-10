from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)  
    weight_class = models.DecimalField(max_digits=5, decimal_places=1)  
    is_title_fight = models.BooleanField(default=False)  
    attendees = models.PositiveIntegerField()  
    location = models.CharField(max_length=255)  
    date = models.DateField()  

    def __str__(self):
        return f"{self.name} - {self.location} ({self.date})"