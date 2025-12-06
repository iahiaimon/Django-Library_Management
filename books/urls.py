from django.urls import path
from .views import (
    home,
    AllBooksView,

)


urlpatterns = [
  path("" , home , name= "home"),
  path("books/" , AllBooksView , name= "books"),
]