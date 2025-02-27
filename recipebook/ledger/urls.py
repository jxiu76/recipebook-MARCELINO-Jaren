from django.urls import path
from .views import recipes, recipe1, recipe2, index

app_name = "ledger"

urlpatterns = [
    path("", index, name="index"), 
    path("recipes/list", recipes, name="recipes"),
    path("recipe/<int:pk>/", recipe_detail, name = "recipe-detail")
]


