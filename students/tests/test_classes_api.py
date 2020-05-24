import uuid

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from students.models import Programme, Class
# from students.serializers import ProgrammeSerializer, ClassSerializer

from core.models import School


def get_sample_school():
    """Create and return sample school for testing"""
    name = str(uuid.uuid4())
    return School.objects.create(
        name=name,
        address='Sandemuni',
        city='Wa',
        region='UW',
    )


def get_sample_programme():
    """Create and return sample class for testing"""
    name = str(uuid.uuid4())
    return Programme.objects.create(
        name=name,
        short_name=name[0:4]
    )


CLASS_URL = reverse('students:class-list')


class PublicClassAPITest(TestCase):
    """Test publicly available api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving classes"""

        res = self.client.get(CLASS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateClassAPITest(TestCase):
    """Test private available api"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@twysolutions.com',
            password='testuserpass',
            school=get_sample_school(),
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_classes_limited_school(self):
        """Test retrieving classes for authenticated user school"""

        class1 = Class.objects.create(
            programme=get_sample_programme(),
            programme_division='A',
            year=1,
            school=self.user.school
        )
        school1 = get_sample_school()

        Class.objects.create(
            programme=get_sample_programme(),
            programme_division='B',
            year=1,
            school=school1
        )

        res = self.client.get(CLASS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['programme_division'], class1.programme_division)

    def test_create_class_success(self):
        """Test creating class successful"""
        prog1 = get_sample_programme()

        payload = {
            'programme': prog1.id,
            'programme_division': 'H',
            'year': 2,
            'school': self.user.school.id
        }

        res = self.client.post(CLASS_URL, payload)

        exists = Class.objects.filter(
            programme_division=payload['programme_division'],
            year=payload['year'],
        ).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
