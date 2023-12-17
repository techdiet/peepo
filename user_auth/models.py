from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
	user = None
	email = models.EmailField(_("email address"), unique=True)
	surname = models.CharField(max_length=50, null=True)
	other_names = models.CharField(max_length=50, null=True)
	dob = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=50, null=True)
	level = models.CharField(max_length=50, null=True)
	gender = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	picture = models.ImageField(upload_to="user_auth/static/", null=True)
	role = models.CharField(max_length=50, null=True)
	PART_TIME = 'part-time'
	FULL_TIME = 'full-time'
	AVAILABILITY_CHOICES = [
        (PART_TIME, 'Part-time'),
        (FULL_TIME, 'Full-time'),
    ]
	availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default=FULL_TIME,
    )
	skills = models.CharField(max_length=50, null=True)
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	class Meta:
		db_table = "employee"
	
	def __str__(self):
		return self.email
	