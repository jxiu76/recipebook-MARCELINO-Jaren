from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [RecipeIngredientLine]

admin.site.register(Recipe, RecipeAdmin)

