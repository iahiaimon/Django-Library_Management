
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reload/", include("django_browser_reload.urls")),
    path("" , include("books.urls")),
    path("user/" , include("accounts.urls")),
]
