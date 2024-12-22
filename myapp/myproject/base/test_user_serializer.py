from rest_framework.test import APITestCase
from api.serializers import UserSerializer

class UserSerializerTest(APITestCase):
    def test_user_serializer(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'password123',
            'role': 'student'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(validated_data['name'], 'Test User')
        self.assertEqual(validated_data['email'], 'test@example.com')
