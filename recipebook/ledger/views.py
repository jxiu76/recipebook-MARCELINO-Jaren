from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe

def index(request):
    return HttpResponse("")

def recipes(request):
    recipe_list = Recipe.objects.all()
    ctx = {"recipes" : recipe_list}
    return render(request, "ledger/recipes.html", ctx)
    
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe" : recipe }

    return render(request, "ledger/recipeMerge.html", ctx)





