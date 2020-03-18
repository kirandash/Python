from django.shortcuts import render
from .models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects # to get all the data from DB
    return render(request, 'jobs/home.html', {'jobs': jobs}) # render templates/jobs/home.html and passing jobs to html

def username(request):
    return render(request, 'jobs/username.html') # render templates/jobs/username.html