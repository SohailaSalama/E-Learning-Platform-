from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

@login_required # restrict page to authenticated users
def Home(request):
    return render(request, 'index.html')

def RegisterView(request):
    if request.method == "POST":
        if request.method == "POST":
             # getting user inputs from frontend
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            #create flag for error
            user_data_has_error = False

            # make sure email and username are not being used
            if User.objects.filter(username=username).exists():
                 user_data_has_error = True
                 messages.error(request, 'Username already exists')

                 if User.objects.filter(email=email).exists():
                     user_data_has_error = True
                     messages.error(request, 'Email already exists')

            # make aure password is at least 5 characters long
            if len(password) < 5:
                user_data_has_error = True
                messages.error(request, 'Password must be at least 5 characters')

            #Create a new user if there are no errors and redirect to the login page. Else redirect back to the register page with errors
                if not user_data_has_error:
                 new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password,
    )
                 messages.success(request, 'Account created. Login now')
                 return redirect('login')
                else:
                    return redirect('register')


    return render(request, 'register.html')

def LoginView(request):
   if request.method == 'POST':

    # getting user inputs from frontend
     username = request.POST.get('username')
     password = request.POST.get('password')

     
# authenticate credentials
     user = authenticate(request=request, username=username, password=password)
     if user is not None:
        # login user if login credentials are correct
        login(request, user)
        # redirect to home page
        return redirect('home')
     else:
        # redirect back to the login page if credentials are wrong
        messages.error(request, 'Invalid username or password')
        return redirect('login')

   return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')
