from .views import RecipeListView
from django.urls import path

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
]
