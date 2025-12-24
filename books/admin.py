from django.contrib import admin
from .models import Category , AddBook , BorrowBook

# Register your models here.

admin.site.register(Category)
admin.site.register(AddBook)
admin.site.register(BorrowBook)
