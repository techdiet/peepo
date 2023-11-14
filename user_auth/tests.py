from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserManagerTest(TestCase):

	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(email="testuser@here.com", password="th112")
		self.assertEqual(user.email, "normal@user.com")
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)
		try:
			self.assertIsNone(user.username)
		except AttributeError:
			pass
		with self.assertRaises(TypeError):
			User.objects.create_user()
		with self.assertRaises(TypeError):
			User.objects.create_user(email="")
		with self.assertRaises(ValueError):
			User.objects.create_user(email="", password="foo")

	def test_create_superuser(self):
		User = get_user_model()
		superuser = User.objects.create_superuser(email="testsuperuser@here.com", password="th112")
		self.assertEqual(superuser.email, "normal@user.com")
		self.assertTrue(superuser.is_active)
		self.assertTrue(superuser.is_staff)
		self.assertTrue(superuser.is_superuser)
		try:
			self.assertIsNone(superuser.username)
		except AttributeError:
			pass
		with self.assertRaises(TypeError):
			User.objects.create_user()
		with self.assertRaises(TypeError):
			User.objects.create_user(email="")
		with self.assertRaises(ValueError):
			User.objects.create_user(email="", password="foo")
