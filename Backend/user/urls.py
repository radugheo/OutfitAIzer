from django.urls import path

from .views import LoginView, LogoutView, RegisterView, UserView

urlpatterns = [
    path("login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("logout", LogoutView.as_view()),
    path("register", RegisterView.as_view()),
]
