from django.db import models

# Create your models here.

class Housing(models.Model):
    
    organization = models.CharField(max_length=100)
    shelter_name = models.CharField(max_length=100)
    shelter_type = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    latitude = models.DecimalField(max_digits=10,decimal_places=5, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    capacity = models.IntegerField()
    # TODO: rewrite as enum
    # 0 = No, 1 = Yes, 2 = No Information Available
    lgbtq2s_friendly = models.IntegerField(default=2)
    wheelchair_accessible = models.IntegerField(default=2)
    public_transit_accessible = models.IntegerField(default=2)
    women_only = models.IntegerField(default=2)
    food_provided = models.IntegerField(default=2)
    showers_provided =models.IntegerField(default=2)

    # TODO: add ratings for security, comfort, etc.
    rating = models.FloatField()
