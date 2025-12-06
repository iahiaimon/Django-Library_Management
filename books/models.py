from django.db import models
from core.models.time_stamp import TimeStampModel

# Create your models here.


class Category(TimeStampModel):
    title = models.CharField(blank=False, null=False)
    slug = models.SlugField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class AddBook(TimeStampModel):
    title = models.CharField(blank=False, null=False)
    slug = models.SlugField(max_length=255)
    author = models.CharField(blank=False, null=False)
    description = models.TextField()
    isbn = models.CharField(blank=False, null=False, max_length=13)
    publisher = models.CharField(blank=False, null=False)
    publication_date = models.DateField()
    language = models.CharField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="Book Cover" , default = "Book Cover/default_cover.jpg")

    def __str__(self):
        return f"{self.title} -- {self.isbn} by {self.author}"
