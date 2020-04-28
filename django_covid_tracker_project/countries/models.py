from django.db import models

# Create your models here.
# Extending Model class from django.db to create Country class - for Country Model
# Model to match country data from API: https://api.thevirustracker.com/free-api?countryTotal=US - In DB we will save only country code, pinned property, remaining property we will get from API
class Country(models.Model):
    code = models.CharField(max_length=10) # Country Code
    pinned = models.BooleanField() # Pinned or Not Pinned