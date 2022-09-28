from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=1000)

    
    def __str__(self):
        return self.name