from django.test import TestCase
from django.contrib.auth import get_user_model
from dotenv import load_dotenv
import os


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""
        email = "test@mailprov.com"
        password = "TestPassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that new usr's email are normalized"""
        email = "TEst@emailprOV.com"
        user = get_user_model().objects.create_user(email, "TestPassword123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that new enter a valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "TestPassd123")

    def test_create_new_admin(self):
        """Test creating superUser"""
        user = get_user_model().objects.create_admin(
            email="test@mailprov.com",
            password="TestPassword123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
