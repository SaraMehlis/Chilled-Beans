from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, blank=True)
    ingredient = models.TextField()
    instruction = models.TextField()
    nutrition_information = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)