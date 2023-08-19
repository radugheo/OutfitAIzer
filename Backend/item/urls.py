from django.urls import path

from . import views

urlpatterns = [
    path("", views.postItem),
    path("get/<str:type>", views.getItemByType),
]
