from django.db import models
from django.urls import reverse

class Employer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    business_name = models.CharField(max_length=200)
    #subscription_fee = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return self.first_name
    #pub_date = models.DateTimeField("date published")


class JobPosting(models.Model):
    job_title= models.CharField(max_length=200) 
    job_description = models.CharField(max_length=1000)
    start_Date = models.DateField()
    end_Date = models.DateField()
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.job_title
    
    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})
