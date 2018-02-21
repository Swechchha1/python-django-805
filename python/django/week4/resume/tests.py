from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTest(TestCase):
    resume = None
    education1 = None
    experience1 = None

    def setUp(self):
        """
        setUp needed to perform the tests, it is called before every test function.
        """
        resume_test = Resume(first_name = "Swechchha", last_name = "Tiwari")
        resume_test.save()

    def test_full_name(self):
        """
        Test for get_full_name method defined in models.py
        """
        r_test =  Resume.objects.first()
        self.assertEqual(r_test.get_full_name(), "Swechchha Tiwari")

    def test_last_name_first_name(self):
        """
        Test for get_last_name_first_name method defined in models.py
        """
        r_test =  Resume.objects.first()
        self.assertEqual(r_test.get_last_name_first_name(), "Tiwari, Swechchha")

    def test_experience(self):
        """
        Test for get_experience method defined in models.py
        """
        r_test = Resume.objects.first()
        actual = list(r_test.get_experience())
        expected = list(r_test.experience_set.all())
        self.assertEqual(actual,expected)

    def test_education(self):
        """
        Test for get_education method defined in models.py
        """
        r_test = Resume.objects.first()
        actual = list(r_test.get_education())
        expected = list(r_test.education_set.all())
        self.assertEqual(actual,expected)
