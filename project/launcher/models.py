from django.db import models

# Create your models here.

class Housing(models.Model):
    organization = models.CharField(max_length=100)
    shelter_name = models.CharField(max_length=100)
    shelter_type = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    latitude = models.DecimalField(max_digits=10)
    longitude = models.DecimalField(max_digits=10)
    capacity = models.IntegerField()
    
    lgbtq2s_friendly = models.BooleanField()
    wheelchair_accessible = models.BooleanField()
    public_transit_accessible = models.BooleanField()
    women_only = models.BooleanField()
    food_provided = models.BooleanField()
    showers_provided = models.BooleanField()

    # TODO: add ratings for security, comfort, etc.
    rating = models.FloatField()

    