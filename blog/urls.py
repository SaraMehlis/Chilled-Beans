from .views import RecipeListView, SearchResultsView
from django.urls import path, include
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path("accounts/", include("allauth.urls")),
    path('form/', views.recipeform, name='recipeform'),
    path('recipe/edit/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/delete/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]

handler404 = 'blog.views.custom_page_not_found'
