from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Category , AddBook
from .forms import CategoryForm , AddBookForm


# Create your views here.
def home(request):
    return render(request, "books/home.html")


def AllBooksView(request):
    books = AddBook.objects.all()   # get all books
    return render(request, "books/all_books.html", {"books": books})