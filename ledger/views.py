from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect("recipe_list")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("recipe_list")
        else:
            return render(request, "ledger/login.html", {"error": "Invalid credentials"})
    
    return render(request, "ledger/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})
