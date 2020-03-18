from django.db import models

# Create your models here.
class Job(models.Model):
    # creating fields(image, summary) for Job Model
    image = models.ImageField(upload_to='images/') # upload path.
    summary = models.CharField(max_length=200)

    # control what to show on admin screen for job model
    def __str__(self):
        return self.summary