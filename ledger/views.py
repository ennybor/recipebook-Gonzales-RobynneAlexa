from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientFormSet, RecipeImageForm
from django.forms import inlineformset_factory

RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields = ('ingredient', 'quantity'),
    extra = 1,
    can_delete=True
)

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
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    images = recipe.images.all()
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe, "ingredients": ingredients, "images": images})

@login_required
def recipe_add_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.recipe = recipe
            new_image.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/recipe_add_image.html', {'form': form, 'recipe': recipe})

@login_required
def recipe_add(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        image_form = RecipeImageForm(request.POST, request.FILES)

        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for form in formset:
                if form.cleaned_data:
                    ingredient = form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()

            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.recipe = recipe
                image.save()

            return redirect("recipe_detail", recipe_id=recipe.id)

    else:
        recipe_form = RecipeForm()
        formset = RecipeIngredientFormSet()
        image_form = RecipeImageForm()

    return render(request, "ledger/recipe_add.html", {
        "recipe_form": recipe_form,
        "formset": formset,
        "image_form": image_form,
    })
