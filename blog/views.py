from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView 
from django.contrib import messages
from .models import Recipe
from .form import RecipeForm

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

def recipeform(request):
    form = RecipeForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            form.save()
            message = 'Recipe added successfully'
            return render(request, 'blog/confirmation.html', {'message': message})
    else:
        form = RecipeForm()   


    return render(request, 'blog/add_recipe.html', {'form': form})

