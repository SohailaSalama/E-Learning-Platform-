from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from base.models import User, Course, Enrollment, Assignment, Grade
from rest_framework.test import APIClient

# 1. User Model Test
class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name="Test User", email="test@example.com", password="password123")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.role, "student")  # Default role

# 2. Course Model Test
class CourseModelTest(TestCase):
    def test_course_creation(self):
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", password="password123", role="doctor")
        course = Course.objects.create(name="Advanced Programming", description="Learn advanced concepts.", doctor=doctor)
        self.assertEqual(course.name, "Advanced Programming")
        self.assertEqual(course.doctor, doctor)

# 3. Enrollment Model Test
class EnrollmentModelTest(TestCase):
    def test_enrollment_creation(self):
        student = User.objects.create(name="Student A", email="studenta@example.com", password="password123")
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", password="password123", role="doctor")
        course = Course.objects.create(name="Intro to AI", doctor=doctor)
        enrollment = Enrollment.objects.create(student=student, course=course)
        self.assertEqual(enrollment.student, student)
        self.assertEqual(enrollment.course, course)

# 4. Assignment Model Test
class AssignmentModelTest(TestCase):
    def test_assignment_creation(self):
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", password="password123", role="doctor")
        course = Course.objects.create(name="Intro to AI", doctor=doctor)
        assignment = Assignment.objects.create(course=course, title="Assignment 1", description="Solve AI problems.")
        self.assertEqual(assignment.course, course)
        self.assertEqual(assignment.title, "Assignment 1")

# 5. Grade Model Test
class GradeModelTest(TestCase):
    def test_grade_creation(self):
        student = User.objects.create(name="Student B", email="studentb@example.com", password="password123")
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", password="password123", role="doctor")
        course = Course.objects.create(name="Intro to AI", doctor=doctor)
        assignment = Assignment.objects.create(course=course, title="Assignment 1", description="Solve AI problems.")
        grade = Grade.objects.create(assignment=assignment, student=student, grade=85.0)
        self.assertEqual(grade.grade, 85.0)

# 6. Signup View Test
class SignupViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_signup(self):
        response = self.client.post(reverse('signup'), {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)

# 7. Login View Test
class LoginViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@example.com', password='password123')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
