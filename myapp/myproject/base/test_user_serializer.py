from rest_framework import serializers
from base.serializers import UserSerializer

# Define a simple test case for UserSerializer
class UserSerializerTest(TestCase):
    def test_user_serializer_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'password': 'password123',
        }
        
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    
    def test_user_serializer_invalid(self):
        # Missing required field 'email'
        data = {
            'name': 'John Doe',
            'password': 'password123',
        }
        
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)



