from django.urls import path

from . import views

urlpatterns = [
    path("", views.postItem),
    path("all", views.getAllItems),
]
