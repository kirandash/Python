from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects # to get all the data from DB
    return render(request, 'jobs/home.html', {'jobs': jobs}) # render templates/jobs/home.html and passing jobs to html

def detail(request, job_id):
    # print(job_id)
    job_detail = get_object_or_404(Job, pk=job_id) # look in db for Job with pk: primary key set as jobid, if found return an object or 4o4
    return render(request, 'jobs/detail.html', {'job': job_detail})

# def username(request):
#     return render(request, 'jobs/username.html') # render templates/jobs/username.html