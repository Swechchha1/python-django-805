from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTest(TestCase):
    resume = None
    education1 = None
    experience1 = None

    def setUp(self):
        resume_test = Resume(first_name = "Swechchha", last_name = "Tiwari")
        resume_test.save()

    def test_full_name(self):
        r_test =  Resume.objects.first()
        self.assertEqual(r_test.get_full_name(), "Swechchha Tiwari")

    def test_last_name_first_name(self):
        r_test =  Resume.objects.first()
        self.assertEqual(r_test.get_last_name_first_name(), "Tiwari, Swechchha")

    def test_experience(self):
        r_test = Resume.objects.first()
        actual = list(r_test.get_experience())
        expected = list(r_test.experience_set.all())
        self.assertEqual(actual,expected)

    def test_education(self):
        r_test = Resume.objects.first()
        actual = list(r_test.get_education())
        expected = list(r_test.education_set.all())
        self.assertEqual(actual,expected)
