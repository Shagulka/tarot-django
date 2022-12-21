from django.test import Client, TestCase
from django.urls import reverse


class HomepageUrlTest(TestCase):
    def test_homepage(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)
