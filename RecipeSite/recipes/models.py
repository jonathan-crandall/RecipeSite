from django.db import models


# Create your models here.
class Recipe(models.Model):
    food = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=4000)
    instructions = models.CharField(max_length=4000)
    created_on = models.DateTimeField(auto_now_add=True)
