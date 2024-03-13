from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView 
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = "index.html"
    context_object_name = 'recipes'

def about(request):
    return render(request, 'blog/about.html')
    
def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = { 
        'recipe': recipe
    }
    
    return render(request, 'blog/recipe_detail.html', context)
