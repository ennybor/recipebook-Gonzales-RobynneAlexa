from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
@admin.register(Profile)
class ProfileAdmin(admin.ModuleAdmin):
    list_display = ("user", "name", "bio")

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated_on")
    search_fields = ("name", "author__username")
    #inlines = [RecipeIngredientInline]
    list_filter = ("created_on", "updated_on")

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "quantity")
    search_fields = ("recipe__name", "ingredient__name")
