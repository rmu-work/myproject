from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date Of Birth')
    contact_number = models.CharField(max_length=15, null=True, verbose_name='Contact Number')
    residency_status = models.CharField(max_length=50, blank=True, null=True, verbose_name='Residency Status')
    portfolio = models.CharField(max_length=512, blank=True, null=True)

    # University
    is_university = models.BooleanField(default=False, verbose_name='University')
    university_id = models.CharField(max_length=75, blank=True, null=True, verbose_name='University ID')
    university_name = models.CharField(max_length=256, blank=True, null=True, verbose_name='University Name')
    website = models.CharField(max_length=256, blank=True, null=True)

    # Common
    profile_picture = models.FileField(upload_to='profile/', blank=True, null=True, verbose_name='Profile Picture')

    country = models.CharField(max_length=75, blank=True, null=True, verbose_name='Country')
    state = models.CharField(max_length=75, blank=True, null=True, verbose_name='State')
    address = models.TextField(blank=True, null=True, verbose_name='Address')

    def __str__(self):
        return self.get_full_name() or self.username
