from django.db import models


# Create your models here.
class Task(models.Model):
     name = models.CharField(max_length=120, unique=True)
     description = models.TextField(blank=True)
     iscompleted = models.BooleanField(default=False)
    
     class Meta:
        ordering = ['name']
  
  
     def __str__(self):
           return self.name
              
                               