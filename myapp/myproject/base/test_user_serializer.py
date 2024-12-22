# test_user_serializer.py

from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase

class UserSignupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup(self):
        data = {
            "email": "testuser@example.com",
            "password": "securepassword123",
            "username": "testuser"
        }
        # Corrected: Change reverse('register') to reverse('signup')
        response = self.client.post(reverse('signup'), data)  # This should match the 'signup' URL in urls.py
        self.assertEqual(response.status_code, 201)  # Expecting a 201 status code (created)






