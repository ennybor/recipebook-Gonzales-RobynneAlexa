from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Home View
def home(request):
    return HttpResponse("<h1>Welcome to the Recipe Book!</h1><p><a href='/recipes/list'>View Recipes</a></p>")

@login_required(login_url="login") #redirects unauthenticated users to login
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required(login_url="login")
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})
