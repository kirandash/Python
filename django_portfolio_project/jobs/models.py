from django.db import models

# Create your models here.
class Job(models.Model):
    # creating fields(image, summary) for Job Model
    image = models.ImageField(upload_to='images/') # upload path.
    summary = models.CharField(max_length=200)