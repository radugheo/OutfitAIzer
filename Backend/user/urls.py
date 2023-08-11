from django.urls import path

from . import views

urlpatterns = [
    path("login", views.postLogin),
    path("user", views.getUser),
    path("logout", views.getLogout),
    path("register", views.postRegister),
]
