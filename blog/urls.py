from .views import RecipeListView
from django.urls import path
from . import views

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
]
