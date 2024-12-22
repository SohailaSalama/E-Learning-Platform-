from django.test import TestCase
from unittest import mock
from base.models import Course, User
from api.serializers import CourseSerializer

class CourseSerializerTest(TestCase):

    @mock.patch('base.models.User.objects.create')  # Mocking User model
    def test_course_serializer_valid(self, mock_user_create):
        # Mock the User creation
        mock_user_create.return_value = User(name="Dr. Smith", email="drsmith@example.com", role="doctor")

        # Create course data
        course_data = {
            'name': 'Test Course',
            'description': 'This is a test course.',
            'doctor': mock_user_create.return_value  # Use the mocked User instance
        }

        # Serialize the course data
        serializer = CourseSerializer(data=course_data)
        
        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

