from django.db import models

# Create your models here.
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title # this is to help us see the size information in forms and in admin panel of django. 

class Order(models.Model):
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # ForeignKey from class Size and on delete we are CASCADING which means if the item gets deleted we will delete all the places the item exists as an Object