from django.db import models

# Create your models here.

class Housing(models.Model):
    organization = models.CharField(max_length=100)
    shelter_name = models.CharField(max_length=100)
    shelter_type = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    capacity = models.IntegerField()
    rating = models.FloatField()
    # add other fields like LGBTQ-friendly, pet-friendly, showers provided, food provided, etc.
    # lgbtq_friendly = models.BooleanField()
