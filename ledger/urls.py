from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("recipes/list/", views.recipe_list, name='recipe_list'),
    path("recipes/<int:recipe_id>/", views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/add_image/', views.recipe_add_image, name='recipe_add_image'),
    path("recipe/add/", views.recipe_add, name="recipe_add"),
    path("logout/", views.logout_view, name="logout"),
]
