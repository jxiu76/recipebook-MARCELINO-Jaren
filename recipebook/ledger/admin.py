from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated_on")
    inlines = [RecipeIngredientInline]
    search_fields = ("name", "author__username")
    list_filter = ("created_on", "updated_on")


# Ingredient Admin
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# Profile Inline for User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"


# Custom User Admin with Profile
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


# Register only Recipe and Ingredient (No RecipeIngredient tab)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
