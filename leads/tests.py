from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


class LandingPageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse("landing-page"))
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")

    # def test_template_neme(self):
    #     pass

