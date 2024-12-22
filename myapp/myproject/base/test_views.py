from django.test import TestCase
from django.urls import reverse

class ViewTests(TestCase):

    def test_homepage_status(self):
        response = self.client.get(reverse('homepage'))  # Replace 'homepage' with your actual URL name
        self.assertEqual(response.status_code, 200)
