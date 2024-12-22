from unittest import mock
from django.test import TestCase
from base.models import User

class UserModelTest(TestCase):
    @mock.patch('base.models.User.objects.create')
    def test_user_creation(self, mock_create):
        # Mocking User model creation
        mock_create.return_value = User(name="Test User", email="test@example.com")
        
        user = User.objects.create(name="Test User", email="test@example.com")
        
        # Check if mock create was called with expected parameters
        mock_create.assert_called_with(name="Test User", email="test@example.com")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
from rest_framework.test import APITestCase
from base.models import User
from api.serializers import UserSerializer


class UserSerializerTest(APITestCase):
    def test_user_serializer(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'password123',
            'role': 'student',
        }
        
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test User')
        self.assertEqual(serializer.validated_data['email'], 'test@example.com')
