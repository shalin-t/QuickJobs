from django.db import models

class Worker(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    skills = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.first_name
    #pub_date = models.DateTimeField("date published")
