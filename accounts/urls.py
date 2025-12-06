from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView,
    UserLogoutView

)


urlpatterns = [
    path("register/" , UserSignupView , name = "register"),
    path("login/" , UserLoginView , name = "login"),
    path("logout/" , UserLogoutView , name = "logout"),
]