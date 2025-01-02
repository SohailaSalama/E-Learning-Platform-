from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from assignments.models import Assignment
from users.models import Profile

@login_required
def dashboard(request):
    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    # If the user is a student
    if request.user.role == 'student':
        # Get enrolled courses and assignments for the student
        enrolled_courses = Course.objects.filter(students=request.user)
        assignments = Assignment.objects.filter(course__in=enrolled_courses)  # Fetch assignments
        context = {
            'profile': profile,
            'enrolled_courses': enrolled_courses,
            'assignments': assignments,
        }
        return render(request, 'users/student_dashboard.html', context)

    # If the user is a teacher
    elif request.user.role == 'teacher':
        # Get courses taught by the teacher
        teacher_courses = Course.objects.filter(teacher=request.user)
        context = {
            'profile': profile,
            'teacher_courses': teacher_courses,
        }
        return render(request, 'users/teacher_dashboard.html', context)

    # If the user's role is invalid
    else:
        messages.error(request, "Invalid role. Please contact support.")
        return redirect('login')
