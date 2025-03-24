from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeImageInline(admin.TabularInline):  # Allows adding images inside Recipe admin
    model = RecipeImage
    extra = 1  # Show one empty form for new images


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated_on")
    inlines = [RecipeIngredientInline, RecipeImageInline]  # Now includes RecipeImage
    search_fields = ("name", "author__username")
    list_filter = ("created_on", "updated_on")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class RecipeImageAdmin(admin.ModelAdmin):  # Optional: Manage images separately
    list_display = ("recipe", "image", "description")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)  # Register RecipeImage separately
