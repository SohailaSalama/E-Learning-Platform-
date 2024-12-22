from django.test import TestCase
from unittest import mock
from base.models import User
from api.serializers import UserSerializer

class UserSerializerTest(TestCase):

    @mock.patch('base.models.User.objects.create')  # Mock User creation
    def test_user_serializer_valid(self, mock_user_create):
        # Mock User creation
        mock_user_create.return_value = User(name="Test User", email="testuser@example.com", role="student")

        # Create user data
        user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'password123',
            'role': 'student'
        }

        # Serialize the user data
        serializer = UserSerializer(data=user_data)

        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

