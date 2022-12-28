from django.db import models
from django.utils.timezone import now

# Create your models here.
class Task(models.Model):
     name = models.CharField(max_length=120, unique=True)
     description = models.TextField(blank=True)
  
     
    #   def __str__(self):
     def __str__(self):
           return self.name
              
                               