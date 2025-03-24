from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes.html"
    context_object_name = "recipes"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipeMerge.html"
    context_object_name = "recipe"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("ledger:recipe-list")


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_image_form.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]  # Link image to the recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ledger:recipe-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.get(
            pk=self.kwargs["pk"]
        )  # Pass the recipe object
        return context
