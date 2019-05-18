from django.db import models
from oscar.apps.customer.abstract_models import AbstractUser
import datetime
from django.utils import timezone

class User(AbstractUser):
	email = models.EmailField(unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	phone_number = models.IntegerField(blank=True)
	date_joined = models.DateTimeField(default = timezone.now)
	store_name = models.CharField(max_length=255, blank=True)
	address_line1 = models.CharField(max_length=255, blank=True)
	address_line2 = models.CharField( max_length=255, blank=True)
	pin_code = models.IntegerField(blank=True)
	district = models.CharField(max_length=255, blank=True)
	state = models.CharField(max_length=255, blank=True)
	pan_number = models.CharField(max_length=255, blank=True)
	gst_number = models.CharField(max_length=255, blank=True)

from oscar.apps.customer.models import *
