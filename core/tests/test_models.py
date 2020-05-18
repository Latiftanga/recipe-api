from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='user@twysolutions.com', password='testpass'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_email_successful(self):
        """Should create user given a unique email"""
        email = 'test@latifappdev.com'
        password = 'Test@pass'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """shoud normalized new email"""
        email = 'test@LATIFAPPDEV.COM'
        user = get_user_model().objects.create_user(email, password='test@123')
        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """should raise error if email is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_new_superuser(self):
        """should create new super user"""
        user = get_user_model().objects.create_superuser('superuser@eg.com', 'super@pass')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representaion"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        """Test the ingredient string representaion"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushrooms sauce',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)
