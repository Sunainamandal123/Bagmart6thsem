from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError

'''
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        help_text="Enter your first name.", 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        help_text="Enter your last name.", 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True, 
        help_text="Enter a valid email address.", 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not re.match("^[A-Za-z ]+$", first_name):
            raise forms.ValidationError("First name should contain only alphabets and spaces.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not re.match("^[A-Za-z ]+$", last_name):
            raise forms.ValidationError("Last name should contain only alphabets and spaces.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean_password(self):
       password = self.cleaned_data.get("password")
       if len(password) < 8:
        raise forms.ValidationError("Password must be at least 8 characters long.")
       if not any(char.isdigit() for char in password):
        raise forms.ValidationError("Password must contain at least one digit.")
       if not any(char.isalpha() for char in password):
        raise forms.ValidationError("Password must contain at least one letter.")
       if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/" for char in password):
        raise forms.ValidationError("Password must contain at least one special character.")
       return password       
'''


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email Address'}),
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email



    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return cleaned_data
    

