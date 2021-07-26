from django.db import models
from accounts.models import TimeStamp
from .tuples import JOB_TYPE, EXPERINCE_LEVEL

class Job(TimeStamp):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    # location
    # employer
    job_description = models.TextField(max_length=1000)
    vacancies = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience_level = models.CharField(max_length=50, choices=EXPERINCE_LEVEL)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categories')
    filled = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name