from django.db import models
from django.shortcuts import render
from .models import Job
# Create your views here.

def list_jobs(request):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render(request, 'job/jobs.html', context)


def job_detail(request, job_id):
    job = Job.objects.get(id=int(job_id))
    context = {'job': job}
    return render(request, 'job/job_detail.html', context)