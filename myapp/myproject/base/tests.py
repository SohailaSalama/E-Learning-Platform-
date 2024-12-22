from django.test import TestCase
from unittest import mock
from api.serializers import UserSerializer, CourseSerializer, EnrollmentSerializer, AssignmentSerializer, GradeSerializer
from base.models import User, Course, Enrollment, Assignment, Grade


# 1. Mocking database for User model creation
class UserModelTest(TestCase):
    @mock.patch('base.models.User.objects.create')
    def test_user_creation(self, mock_create):
        # Mock the return value of User.objects.create()
        mock_create.return_value = User(name="Test User", email="test@example.com")

        # Call the method you want to test
        user = User.objects.create(name="Test User", email="test@example.com")

        # Assert that the mock method was called and the mock object was returned
        mock_create.assert_called_with(name="Test User", email="test@example.com")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")


# 2. Testing Course model creation (without database)
class CourseModelTest(TestCase):
    @mock.patch('base.models.Course.objects.create')
    def test_course_creation(self, mock_create):
        # Mock the return value of Course.objects.create()
        mock_create.return_value = Course(name="Test Course", description="A test course")

        # Call the method you want to test
        course = Course.objects.create(name="Test Course", description="A test course")

        # Assert that the mock method was called and the mock object was returned
        mock_create.assert_called_with(name="Test Course", description="A test course")
        self.assertEqual(course.name, "Test Course")
        self.assertEqual(course.description, "A test course")


# 3. Testing Assignment model creation (without database)
class AssignmentModelTest(TestCase):
    @mock.patch('base.models.Assignment.objects.create')
    def test_assignment_creation(self, mock_create):
        # Mock the return value of Assignment.objects.create()
        mock_create.return_value = Assignment(title="Test Assignment", course_id=1)

        # Call the method you want to test
        assignment = Assignment.objects.create(title="Test Assignment", course_id=1)

        # Assert that the mock method was called and the mock object was returned
        mock_create.assert_called_with(title="Test Assignment", course_id=1)
        self.assertEqual(assignment.title, "Test Assignment")
        self.assertEqual(assignment.course_id, 1)


# 4. Testing Grade model creation (without database)
class GradeModelTest(TestCase):
    @mock.patch('base.models.Grade.objects.create')
    def test_grade_creation(self, mock_create):
        # Mock the return value of Grade.objects.create()
        mock_create.return_value = Grade(grade=90, student_id=1, assignment_id=1)

        # Call the method you want to test
        grade = Grade.objects.create(grade=90, student_id=1, assignment_id=1)

        # Assert that the mock method was called and the mock object was returned
        mock_create.assert_called_with(grade=90, student_id=1, assignment_id=1)
        self.assertEqual(grade.grade, 90)
        self.assertEqual(grade.student_id, 1)
        self.assertEqual(grade.assignment_id, 1)


# 5. Testing Enrollment model creation (without database)
class EnrollmentModelTest(TestCase):
    @mock.patch('base.models.Enrollment.objects.create')
    def test_enrollment_creation(self, mock_create):
        # Mock the return value of Enrollment.objects.create()
        mock_create.return_value = Enrollment(course_id=1, student_id=1)

        # Call the method you want to test
        enrollment = Enrollment.objects.create(course_id=1, student_id=1)

        # Assert that the mock method was called and the mock object was returned
        mock_create.assert_called_with(course_id=1, student_id=1)
        self.assertEqual(enrollment.course_id, 1)
        self.assertEqual(enrollment.student_id, 1)


# 6. Testing the User serializer (without database)
class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        # Test serialization of a user
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'password123',
            'role': 'student'
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # Test deserialization (validating the user data)
        user_data = serializer.validated_data
        self.assertEqual(user_data['name'], 'Test User')
        self.assertEqual(user_data['email'], 'test@example.com')


# 7. Testing the Course serializer (without database)
class CourseSerializerTest(TestCase):
    def test_course_serializer(self):
        # Mock a User instance for the 'doctor' field
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", password="password123", role="doctor")
        
        # Test serialization of a course with the 'doctor' field provided by its pk (ID)
        data = {
            'name': 'Test Course',
            'description': 'A description of the test course',
            'doctor': doctor.id,  # Use doctor.id here, which is the primary key (pk) of the User instance
        }

        serializer = CourseSerializer(data=data)

        # Print the validation errors if any
        if not serializer.is_valid():
            print(serializer.errors)

        # Assert that the serializer is valid now
        self.assertTrue(serializer.is_valid())

        # Test deserialization (validating the course data)
        course_data = serializer.validated_data
        self.assertEqual(course_data['name'], 'Test Course')
        self.assertEqual(course_data['description'], 'A description of the test course')
        self.assertEqual(course_data['doctor'], doctor)
