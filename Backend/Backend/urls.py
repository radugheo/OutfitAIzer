from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("user/", include("user.urls")),
    path("item/", include("item.urls")),
    path("outfit/", include("outfit.urls")),
]
