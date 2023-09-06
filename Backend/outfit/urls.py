from django.urls import path

from . import views

urlpatterns = [
    path("all", views.getOutfits),
    path("rate/<int:id>", views.postRate),
]
