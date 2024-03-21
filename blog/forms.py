from django import forms
from .models import Recipe
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    ingredient = forms.CharField(widget=forms.Textarea)
    instruction = forms.CharField(widget=forms.Textarea)
    nutrition_information = forms.CharField(widget=forms.Textarea)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        model = Recipe
        fields = [
            'title',
            'ingredient',
            'instruction',
            'nutrition_information',
            'image',
            ]
