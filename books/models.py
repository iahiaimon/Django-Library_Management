from django.db import models
from core.models.time_stamp import TimeStampModel
from django.conf import settings

from accounts.models import CustomUser
from django.utils import timezone
from datetime import timedelta

# Create your models here.


from django.db import models
from django.utils.text import slugify


class Category(TimeStampModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    cat_image = models.ImageField(
        upload_to="Category_Image", default="Category_Image/default_category.jpg"
    )
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:  # only set slug if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AddBook(TimeStampModel):
    title = models.CharField(blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.CharField(blank=False, null=False)
    description = models.TextField()
    isbn = models.TextField(blank=False, null=False)
    publisher = models.CharField(blank=False, null=False)
    publication_date = models.DateField()
    language = models.CharField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to="Book Cover", default="Book Cover/default_cover.jpg"
    )

    def save(self, *args, **kwargs):
        if not self.slug:  # only set slug if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -- {self.isbn} by {self.author}"


DEFAULT_LOAN_DAYS = 15

class BorrowBook(TimeStampModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="borrowed_books",
    )
    book = models.ForeignKey(
        AddBook,  # adjust import/path if necessary
        on_delete=models.CASCADE,
        related_name="borrowings",
    )
    isbn = models.CharField(blank=False, null=False)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        ordering = ["-borrow_date"]

    def __str__(self):
        return f"{self.user} — {self.book} (due {self.return_date})"

    def save(self, *args, **kwargs):
        # On first save (no return_date), set default return_date to borrow_date + DEFAULT_LOAN_DAYS
        if not self.return_date:
            # if borrow_date present (auto_now_add ensures it's set on creation)
            borrow_date = self.borrow_date or timezone.now().date()
            self.return_date = borrow_date + timedelta(days=DEFAULT_LOAN_DAYS)
        super().save(*args, **kwargs)

    def extend(self, days: int = DEFAULT_LOAN_DAYS, by_admin: bool = True):
        """
        Extend the return_date by `days`. by_admin param is informative only;
        permission checks should be performed in view/admin where this is called.
        """
        if not self.return_date:
            # in case return_date somehow missing, set baseline from borrow_date
            baseline = self.borrow_date or timezone.now().date()
            self.return_date = baseline + timedelta(days=days)
        else:
            self.return_date = self.return_date + timedelta(days=days)
        self.save()
        return self.return_date

    @property
    def is_overdue(self):
        if not self.return_date:
            return False
        return (timezone.now().date() > self.return_date) and not self.is_returned
