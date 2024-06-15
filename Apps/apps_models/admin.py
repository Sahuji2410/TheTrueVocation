from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CareersBucketBaseUser)
admin.site.register(JobDescription)
admin.site.register(JobType)
admin.site.register(jobAnnouncments)