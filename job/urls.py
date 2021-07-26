from django.urls import path
from .views import *

urlpatterns = [
    path('', list_jobs, name='list-jobs'),
    path('<int:job_id>/', job_detail, name='job_detail')
]
