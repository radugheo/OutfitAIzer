from django.urls import path

from . import views

urlpatterns = [
    path("", views.postItem),
    path("<str:type>", views.getItemByType),
]
