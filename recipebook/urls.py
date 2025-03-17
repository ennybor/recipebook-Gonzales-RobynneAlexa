from django.contrib import admin
from django.urls import path, include
#from ledger import views  


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ledger.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
