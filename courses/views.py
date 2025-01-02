from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course
from .forms import CourseForm
from .models import Assignment , Submission
from django.http import HttpResponse

# List all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# Create a new course (for teachers only)
@login_required
def course_create(request):
    if request.user.role != 'teacher':  # Only teachers can create courses
        messages.error(request, "You are not authorized to create courses.")
        return redirect('course_list')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user  # Set the logged-in user as the instructor
            course.save()
            messages.success(request, "Course created successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'courses/course_create.html', {'form': form})

# Enroll a student in a course
@login_required
def course_enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user.role != 'student':  # Only students can enroll
        messages.error(request, "You are not authorized to enroll in courses.")
        return redirect('course_list')

    if request.user in course.students.all():
        messages.info(request, "You are already enrolled in this course.")
    else:
        course.students.add(request.user)
        messages.success(request, f"You have successfully enrolled in {course.title}.")

    return redirect('course_list')

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})
    
@login_required
def submit_assignment(request, assignment_id):
    # Fetch the assignment based on ID
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    if request.method == 'POST':
        # Handle file upload or form submission here
        # For example:
        submitted_file = request.FILES.get('file')  # Replace 'file' with your form field name
        if submitted_file:
            # Save the file or submission (extend this part based on your logic)
            # assignment.submission = submitted_file
            # assignment.save()
            pass
        
        # Redirect to a success page or back to the course/assignment page
        return redirect('success_page')  # Replace 'success_page' with an actual URL name or path
    
    # Render the submission form
    return render(request, 'courses/submit_assignment.html', {'assignment': assignment})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'courses/assignment_list.html', {'assignments': assignments})

def grade_assignment(request, submission_id):
    """
    This view handles grading of a specific assignment submission.
    It retrieves the submission, allows a grade to be entered via POST, and saves the grade.
    """
    # Retrieve the submission object from the database
    submission = get_object_or_404(Submission, id=submission_id)
    assignment = submission.assignment  # Assuming Submission has a foreign key to Assignment

    if request.method == "POST":
        # Get the grade from the POST request
        grade = request.POST.get("grade")

        if not grade:
            return HttpResponse("Grade is required.", status=400)

        # Save the grade to the submission
        submission.grade = grade
        submission.graded_by = request.user  # Assuming the user grading is the logged-in user
        submission.save()

        # Return a success message
        return HttpResponse(f"Assignment '{assignment.title}' submission graded successfully with grade: {grade}")

    # Render the grading form in case of GET request
    return render(request, 'courses/grade_assignment.html', {
        'submission': submission,
        'assignment': assignment
    })

def some_function(request):
    return HttpResponse("This is a test function.")