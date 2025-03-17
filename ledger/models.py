'''
Create a Profile model by extending the default User model, which has the following:
Name - at most 50 characters
Bio - at most 255 character

Modify the recipe model to contain the following:
an Author field
a CreatedOn field that is automatically added upon creation of the instance
an UpdatedOn field that is automatically updated 
(Note: You don't have to modify the save function, 
which might be what the internet may tell you)
'''

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name or self.user.username 

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.id)])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
