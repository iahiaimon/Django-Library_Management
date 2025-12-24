from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Category, AddBook , BorrowBook
from .forms import CategoryForm, AddBookForm ,BorrowBookForm


# Create your views here.
def home(request):
    return render(request, "books/home.html")

def AllBooksView(request):

    books = AddBook.objects.all()  # get all books
    return render(request, "books/all_books.html", {"books": books})


def BorrowBooksFormView(request):
    form = BorrowBookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(request , "books")
    return render(request , "books/borrow_form.html")
