from django.test import TestCase
from rest_framework.exceptions import ValidationError
from base.serializers import UserSerializer

class UserSerializerTest(TestCase):

    def test_valid_user_serializer(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'password123',
            'role': 'admin'
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test User')
        self.assertEqual(serializer.validated_data['email'], 'test@example.com')
    
    def test_invalid_user_serializer(self):
        data = {
            'name': '',
            'email': 'invalid-email',
            'password': 'short',
            'role': 'admin'
        }
        serializer = UserSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)


