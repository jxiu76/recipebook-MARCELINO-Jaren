from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipeMerge.html"
