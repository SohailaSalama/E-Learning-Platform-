from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile
from .forms import UserRegistrationForm
from courses.models import Course, Assignment

@login_required
def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)

            if created:
                messages.success(request, "Registration successful!")
            else:
                messages.warning(request, "User already has a profile.")

            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.user.role == 'student':
        # Fetch enrolled courses for the student
        enrolled_courses = Course.objects.filter(students=request.user)

        # Fetch assignments related to the enrolled courses
        assignments = Assignment.objects.filter(course__in=enrolled_courses)

        context = {
            'profile': profile,
            'enrolled_courses': enrolled_courses,
            'assignments': assignments,
        }
        return render(request, 'users/student_dashboard.html', context)

    elif request.user.role == 'teacher':
        # Fetch courses taught by the teacher
        teacher_courses = Course.objects.filter(teacher=request.user)

        context = {
            'profile': profile,
            'teacher_courses': teacher_courses,
        }
        return render(request, 'users/teacher_dashboard.html', context)

    else:
        messages.error(request, "Invalid role. Please contact support.")
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('/users/login/')

# Create or retrieve a user and profile for testing purposes
user, user_created = User.objects.get_or_create(
    username="hanaelashry",
    defaults={
        "password": "hana1234",  # Use proper password hashing in production
        "role": "student",
    }
)
print("User:", user)
print("Was the user created now?", user_created)

profile, profile_created = Profile.objects.get_or_create(user=user)
print("Profile:", profile)
print("Was the profile created now?", profile_created)
