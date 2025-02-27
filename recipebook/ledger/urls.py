from django.urls import path
from .views import recipes, recipe_detail, index 

app_name = "ledger"

urlpatterns = [
    path("", index, name="index"), 
    path("recipes/list", recipes, name="recipes"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe-detail")
]

