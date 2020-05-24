import uuid

from django.test import TestCase

from students import models


def create_sample_programme():
    name = str(uuid.uuid4())

    return models.Programme.objects.create(
        name=name,
        short_name=name[0:4]
    )


class StudentsModelTest(TestCase):

    def test_programme_str(self):
        """Test the string representation of programme"""

        programme = models.Programme.objects.create(name='Arts')

        self.assertEqual(str(programme), programme.name)

    def test_klass_str(self):
        """Test the string representation of klass"""

        klass = models.Class.objects.create(
            programme=create_sample_programme(),
            programme_division='A',
            year=1
        )

        self.assertEqual(str(klass), f'{klass.programme.short_name} {klass.year} {klass.programme_division}')
