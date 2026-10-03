from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
