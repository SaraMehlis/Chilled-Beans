from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView 
from django.contrib import messages
from .models import Recipe
from .form import RecipeForm
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = "index.html"
    context_object_name = 'recipes'

#def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['recipes'] = Recipe.objects.all()  
#        return context

def about(request):
    return render(request, 'blog/about.html')
    
def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = { 
        'recipe': recipe,
        'user': request.user  # Pass the current user to the context to show edit and delete button
    }
    
    return render(request, 'blog/recipe_detail.html', context)

def recipeform(request):
    form = RecipeForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.slug = slugify(recipe.title) 
            form.save()
            message = 'Recipe added successfully'
            return render(request, 'blog/confirmation.html', {'message': message})
    else:
        form = RecipeForm()   


    return render(request, 'blog/add_recipe.html', {'form': form})

def edit_recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    form = RecipeForm(request.POST or None, request.FILES or None,  instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/edit_recipe.html', {'form': form, 'recipe': recipe})

def delete_recipe(request, slug):
    recipe = Recipe.objects.filter(slug=slug)
    recipe.delete()
    message = 'Recipe deleted successfully.'
    context = {'message': message,
               'recipe': recipe}

    return render(request, 'blog/delete.html', context)

class SearchResultsView(ListView):
    template_name = 'blog/search_results.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(instruction__icontains=query) |
                Q(ingredient__icontains=query) 
            )
        else:
            recipes = Recipe.objects.all()
               

        return recipes