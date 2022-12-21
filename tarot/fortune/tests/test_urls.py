from django.test import TestCase
from django.urls import reverse


class FortuneUrlTest(TestCase):
    def test_feedback_url(self):
        response = self.client.get(reverse('fortune:fortune_list'))
        self.assertEqual(response.status_code, 302)
