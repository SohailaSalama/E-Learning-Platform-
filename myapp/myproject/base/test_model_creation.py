from unittest import mock
from django.test import TestCase
from base.models import User

class UserModelTest(TestCase):
    @mock.patch('base.models.User.objects.create')  # Mocking the User model
    def test_create_user(self, mock_create):
        # Mock user creation
        mock_create.return_value = User(name="Test User", email="testuser@example.com", password="password123", role="student")

        # Create user using the mock
        user = User.objects.create(name="Test User", email="testuser@example.com", password="password123", role="student")

        # Check if the mock method was called and the mock object was returned
        mock_create.assert_called_with(name="Test User", email="testuser@example.com", password="password123", role="student")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "testuser@example.com")
