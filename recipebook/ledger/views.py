from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipeMerge.html'

def index(request):
    return HttpResponse("")

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes" : recipes}
    return render(request, "ledger/recipes.html", ctx)
    
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe" : recipe }

    return render(request, "ledger/recipeMerge.html", ctx)





