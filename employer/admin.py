from django.contrib import admin

from .models import Employer
from .models import JobPosting
# Register your models here.
admin.site.register(Employer)
admin.site.register(JobPosting)