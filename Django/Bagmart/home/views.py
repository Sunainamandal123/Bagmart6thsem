from django.shortcuts import render, redirect 
#from django.urls import reverse_lazy
#from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from .forms import RegistrationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

def home(request):
    return render(request ,'index.html')




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User  

def customerlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=username)  # Fetch user by email
        except User.DoesNotExist:
            messages.error(request, "User does not exist. Please register.")
            return render(request, 'customerlogin.html')

        user = authenticate(request, username=user.username, password=password)  # Authenticate

        if user is not None:
            login(request, user)
            return redirect('main')  # Redirect to homepage
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'customerlogin.html')
        




from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email'].split('@')[0]  # Use the email before '@' as the username
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect('main')  
        else:
            print("Form errors:", form.errors)  
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})






from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  
    request.session.flush()  # session cookie lai dlt garxa

    # automatic re-login garnu didaina
    response = redirect('index')
    response.delete_cookie('sessionid')  #  session cookie lai dlt garxa

    return response



'''from .models import Product 

def main(request):
    products = Product.objects.all()  # Keep this as 'products' instead of 'images'
    
    context = {
        'products': products  # Pass 'products' here
    }
    
    return render(request, 'main.html', context)'''
    
from .models import Product

def main(request):
    featured_products = Product.objects.filter(is_featured=True, is_published=True)
    new_products = Product.objects.filter(is_new=True, is_published=True)

    context = {
        'featured_products': featured_products,
        'new_products': new_products
    }

    return render(request, 'main.html', context)

#bag Shop page

from django.shortcuts import render
from .models import Bag

def shop(request):
    category = request.GET.get('category', 'All products')  # Get category from URL parameter
    if category == 'All products':
        products = Bag.objects.all()
    else:
        products = Bag.objects.filter(category=category)  # Filter products by selected category

    context = {
        'products': products,
        'selected_category': category
    }
    return render(request, 'shop.html', context)


def Aboutus(request):
    return render(request ,'Aboutus.html')