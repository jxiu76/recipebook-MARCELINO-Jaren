from django.db import models
from django.urls import reverse 
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[self.pk])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="used_in_recipes")
    quantity = models.CharField(max_length=100)  # Can store "2 cups", "1 tbsp", etc.

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"