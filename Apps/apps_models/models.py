from django.db import models
from .model_manager import CareersBucketBaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choices import *
import string
import random
from django.utils import timezone
from django.conf import settings

class CommonTimePicker(models.Model):
    """
    An abstract model in Django that provides two fields, `created_at` and `updated_at`, which automatically record the date and time when an object is created or updated.
    """
    created_at = models.DateTimeField("Created Date", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True, db_index=True)
    class Meta:
        abstract = True

class CareersBucketBaseUser(AbstractBaseUser,CommonTimePicker,PermissionsMixin):
    user_type = models.CharField("User Type",max_length=10,default="User",choices=USER_TYPE_CHOICES,db_index=True)
    email = models.EmailField(('email address'), unique=True, db_index=True)
    full_name = models.CharField(('full name'), max_length=255, blank=True, null=True, db_index=True)
    profile_picture = models.ImageField("profile picture",upload_to='profile_images/', null=True, blank=True)

    phone_number = models.CharField("Phone Number",max_length=20,blank=True,null=True,db_index=True)

    is_active = models.BooleanField(('active'), default=True, db_index=True)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_superuser = models.BooleanField(('superuser status'), default=False)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CareersBucketBaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        super(CareersBucketBaseUser, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_joined']
    
class JobType(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class JobDescription(models.Model):

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, related_name='job_descriptions')
    experience_level = models.CharField('Experience required ',max_length=150,default="Entry Lever")
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_postings')
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    company_picture = models.ImageField("company picture",upload_to='company_images/', null=True, blank=True)


    def __str__(self):
        return self.title
    

class jobAnnouncments(models.Model):
    announment_title = models.CharField(max_length=150,blank=True,null=True,default="No Announcements!")
    description = models.TextField(max_length=500,blank=True)
    youtube_link = models.URLField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.announment_title