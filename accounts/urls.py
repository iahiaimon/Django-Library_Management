from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView

)


urlpatterns = [
    path("register/" , UserSignupView , name = "register"),
    path("login/" , UserLoginView , name = "register"),
]