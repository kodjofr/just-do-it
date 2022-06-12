from pyexpat import model
from django.db import models


# Task Model

class Task(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

