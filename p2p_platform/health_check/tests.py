from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):
    def test_all_views(self):
        # Get all URLs defined in your project's URL configuration
        urls = [
            reverse('health'),
            reverse('isMoneroUp'),
            # Add more URLs here as needed
        ]

        # Loop through each URL and check if it returns a 200 status code
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)