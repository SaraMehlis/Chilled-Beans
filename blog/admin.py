from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

#class RecipeAdmin(SummernoteModelAdmin):


# Register your models here.
admin.site.register(Recipe)