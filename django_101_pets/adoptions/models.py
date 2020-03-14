from django.db import models

# Create your models here.
# Use Model class from django.db to create class
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True) # with blank = True, blank vallues will be stored as zero. Breed will be set as zero for unknown breeds
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) # null=True, so that we can store null value bcoz with blank = True, blank vallues will be stored as zero as for age it will be difficult to differentiate b/w real zero and null. Null age is to mention age for dogs with unknown age
    vaccinations = models.ManyToManyField('Vaccine', blank=True) # ManyToMany relation with Vaccine model as a dog can have many vaccines, blank is true. since a dog might not need any vaccine

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): # string representation of the model
        return self.name # by default on admin Vaccine shows object object which is not very userful. We are telling django to shown the name of the object instead.