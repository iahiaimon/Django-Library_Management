from django.db import models
from core.models.time_stamp import TimeStampModel

# Create your models here.


from django.db import models
from django.utils.text import slugify

class Category(TimeStampModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    cat_image = models.ImageField(upload_to="Category_Image" , default = "Category_Image/default_category.jpg")
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:  # only set slug if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class AddBook(TimeStampModel):
    title = models.CharField(blank=False, null=False)
    slug = models.SlugField(max_length=255 , unique=True , blank= True)
    author = models.CharField(blank=False, null=False)
    description = models.TextField()
    isbn = models.TextField(blank=False, null=False)
    publisher = models.CharField(blank=False, null=False)
    publication_date = models.DateField()
    language = models.CharField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="Book Cover" , default = "Book Cover/default_cover.jpg")

    def save(self, *args, **kwargs):
        if not self.slug:  # only set slug if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -- {self.isbn} by {self.author}"
