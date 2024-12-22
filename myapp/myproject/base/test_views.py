from django.test import TestCase
from django.urls import reverse

class HomepageViewTest(TestCase):
    def test_homepage_status(self):
        # Assuming the URL name is 'homepage'
        response = self.client.get(reverse('homepage'))  
        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully

    def test_homepage_content(self):
        # Ensure that a specific content exists in the homepage
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "Welcome to the homepage")  # Replace with actual content in your homepage
