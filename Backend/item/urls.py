from django.urls import path

from . import views

urlpatterns = [
    path("", views.postItem),
    path("all", views.getItems),
    path("delete/<int:id>", views.postDelete),
    path("get/<str:type>", views.getItemByType),
]
