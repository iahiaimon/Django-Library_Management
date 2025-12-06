from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "phone",
            "image",
            "institute",
            "department",
            "password",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter email address"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter phone number"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Upload your student id card"}
            ),
            "institute": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your institute name"}
            ),
            "department": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Department (e.g., CSE, EEE)",
                }
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a secure password",
                }
            ),
        }
