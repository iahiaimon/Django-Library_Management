from django import forms
from .models import Category, AddBook


class CategoryForm(forms.ModelForm):
    class Meta:
        models = Category
        fields = ("title", "description")


class AddBookForm(forms.ModelForm):
    class Meta:
        models = AddBook
        fields = (
            "title",
            "author",
            "description",
            "isbn",
            "publisher",
            "publication_date",
            "language",
            "category",
            "cover_image",
        )
