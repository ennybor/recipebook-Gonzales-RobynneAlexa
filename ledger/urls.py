from django.urls import path
#from . import views
from .views import recipe_list, recipe_detail, login_view, logout_view

urlpatterns = [
    path("", login_view, name="login"),
    path("recipes/list/", recipe_list, name='recipe_list'),
    path("recipes/<int:recipe_id>/", recipe_detail, name='recipe_detail'),
    path("logout/", logout_view, name="logout"),
]
