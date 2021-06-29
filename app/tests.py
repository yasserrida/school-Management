from django.test import TestCase
from django.utils import timezone
from .models import student
from django.test import Client
from django.urls import reverse


class StudentModelTests(TestCase):
    client = Client()

    def New_Student(self):
        user = student.store(self, 'user', 'user', 'Homme', timezone.now(), 15)
        self.assertEqual(str(user.firstName), 'user')

    def get_all(self):
        all = student.all(self)
        self.assertGreaterEqual(len(all), 0)

    def view_test(self, url):
        response = self.client.get(reverse(str(url)))
        self.assertEqual(response.status_code, 200)
