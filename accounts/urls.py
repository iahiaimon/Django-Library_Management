from django.urls import path
from .views import (
    UserSignupView,

)


urlpatterns = [
    path("register/" , UserSignupView , name = "register")
]