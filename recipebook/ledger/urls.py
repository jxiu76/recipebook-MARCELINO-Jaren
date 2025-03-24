from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeImageCreateView,
)

app_name = "ledger"

urlpatterns = [
    path("recipes/list", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe-add"),
    path(
        "recipe/<int:pk>/add_image/",
        RecipeImageCreateView.as_view(),
        name="recipe-add-image",
    ),
]
