from django.db import models

# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()