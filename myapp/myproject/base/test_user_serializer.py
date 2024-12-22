from django.test import TestCase
from base.serializers import UserSerializer

class UserSerializerTest(TestCase):
    def test_user_serializer_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'password': 'password123',
        }
        # Create a UserSerializer instance
        serializer = UserSerializer(data=data)
        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid(self):
        # Missing required field 'email'
        data = {
            'name': 'John Doe',
            'password': 'password123',
        }
        serializer = UserSerializer(data=data)
        # Check if the serializer is invalid and 'email' is a required field
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)




