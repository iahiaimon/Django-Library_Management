from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
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


def UserLoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")


@login_required
def UserLogoutView(request):
    logout(request)
    messages.success(request , "You are successfully logged out!")
    return redirect("login")
