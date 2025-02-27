from django.db import models
from django.urls import reverse 
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = "ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = "recipe")
    quantity = models.CharField(max_length=100)


