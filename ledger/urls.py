from django.urls import path
#from . import views
from .views import home, recipe_list, recipe_detail

urlpatterns = [
    path("", home, name="home"),
    path("recipes/list/", recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
