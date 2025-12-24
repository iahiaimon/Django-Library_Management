from django.urls import path
from .views import (
    home,
    AllBooksView,
    BorrowBooksFormView
    

)


urlpatterns = [
  path("" , home , name= "home"),
  path("books/" , AllBooksView , name= "books"),
  path("borrow_books/" , BorrowBooksFormView , name= "borrow_books_form"),
]