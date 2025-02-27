from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipeMerge.html'

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes" : recipes}
    return render(request, "recipes.html", ctx)
    
def recipe_detail(request, pk):
    ctx = {"recipe" : Recipe.objects.get(pk=pk) }

    return render(request, "recipeMerge.html", ctx)





