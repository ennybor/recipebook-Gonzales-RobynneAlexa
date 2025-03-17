from django.contrib import admin
from django.urls import path
from ledger import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_view, name="login"),  
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"), 
    path("logout/", views.logout_view, name="logout"),
]
