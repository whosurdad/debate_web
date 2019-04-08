from django.db import models

# Create your models here.

class Games(models.Model):
    description = models.CharField(max_length=100)