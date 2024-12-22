from django.test import TestCase
from base.models import User  # Assuming User model is in the 'base' app

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="testuser@example.com", password="password123")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "testuser@example.com")
