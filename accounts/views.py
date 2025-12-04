from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CustomUser
from .forms import CustomUserForm

def UserSignupView(request):
    # if GET -> show empty form
    if request.method == "GET":
        form = CustomUserForm()
        return render(request, "accounts/signup.html", {"form": form})

    # if POST -> validate and save
    form = CustomUserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])  # hash password
        user.save()  # save the instance we modified

        messages.success(request, f"User {user.username} created successfully.")
        return redirect("home")  # change "home" to your URL name
    else:
        # form invalid -> re-render with errors
        return render(request, "accounts/signup.html", {"form": form})
