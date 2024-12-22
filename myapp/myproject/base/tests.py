from rest_framework import serializers
from django.test import TestCase
from unittest import mock
from api.serializers import UserSerializer, CourseSerializer
from base.models import User, Course, Assignment, Grade, Enrollment


# Mocking the User model to avoid real database interactions
class UserModelTest(TestCase):
    @mock.patch('base.models.User.objects.create')
    def test_user_creation(self, mock_create):
        mock_create.return_value = User(name="Test User", email="test@example.com", role="student")

        user = User.objects.create(name="Test User", email="test@example.com", role="student")

        mock_create.assert_called_with(name="Test User", email="test@example.com", role="student")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")


# Mocking the Course model to avoid real database interactions
class CourseModelTest(TestCase):
    @mock.patch('base.models.Course.objects.create')
    def test_course_creation(self, mock_create):
        mock_create.return_value = Course(name="Test Course", description="A test course", doctor="Dr. Smith")

        course = Course.objects.create(name="Test Course", description="A test course", doctor="Dr. Smith")

        mock_create.assert_called_with(name="Test Course", description="A test course", doctor="Dr. Smith")
        self.assertEqual(course.name, "Test Course")
        self.assertEqual(course.description, "A test course")


# Mocking the Assignment model to avoid real database interactions
class AssignmentModelTest(TestCase):
    @mock.patch('base.models.Assignment.objects.create')
    def test_assignment_creation(self, mock_create):
        mock_create.return_value = Assignment(title="Test Assignment", course_id=1)

        assignment = Assignment.objects.create(title="Test Assignment", course_id=1)

        mock_create.assert_called_with(title="Test Assignment", course_id=1)
        self.assertEqual(assignment.title, "Test Assignment")
        self.assertEqual(assignment.course_id, 1)


# Mocking the Grade model to avoid real database interactions
class GradeModelTest(TestCase):
    @mock.patch('base.models.Grade.objects.create')
    def test_grade_creation(self, mock_create):
        mock_create.return_value = Grade(grade_value=90, student_id=1, assignment_id=1)

        grade = Grade.objects.create(grade_value=90, student_id=1, assignment_id=1)

        mock_create.assert_called_with(grade_value=90, student_id=1, assignment_id=1)
        self.assertEqual(grade.grade_value, 90)
        self.assertEqual(grade.student_id, 1)
        self.assertEqual(grade.assignment_id, 1)


# Mocking the Enrollment model to avoid real database interactions
class EnrollmentModelTest(TestCase):
    @mock.patch('base.models.Enrollment.objects.create')
    def test_enrollment_creation(self, mock_create):
        mock_create.return_value = Enrollment(course_id=1, student_id=1)

        enrollment = Enrollment.objects.create(course_id=1, student_id=1)

        mock_create.assert_called_with(course_id=1, student_id=1)
        self.assertEqual(enrollment.course_id, 1)
        self.assertEqual(enrollment.student_id, 1)


# Testing the Course Serializer without touching the database
class CourseSerializerTest(TestCase):
    def test_course_serializer(self):
        data = {
            'name': 'Test Course',
            'description': 'A description of the test course',
            'doctor': 'Dr. Smith',
        }

        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        course_data = serializer.validated_data
        self.assertEqual(course_data['name'], 'Test Course')
        self.assertEqual(course_data['description'], 'A description of the test course')
        self.assertEqual(course_data['doctor'], 'Dr. Smith')


# Testing the User Serializer without touching the database
class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'role': 'student',
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user_data = serializer.validated_data
        self.assertEqual(user_data['name'], 'Test User')
        self.assertEqual(user_data['email'], 'test@example.com')
        self.assertEqual(user_data['role'], 'student')

