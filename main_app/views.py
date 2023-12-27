from django.shortcuts import render
from works.models import Job


def index(request, job_name):
    
    if request.method == 'POST':
        current_job = Job.objects.get(title=job_name)
        description = request.POST['description']
        category = request.POST['category']
        location = request.POST['location']
        employer = request.POST['employer']
        created_at = request.POST['created_at']
        min_salary = request.post['min_salary']
        max_salary = request.post['max_salary']
        
        jobs = Job.objects.filter(location_province=location,job_category=category)

        t_list ={
            'jobs' : jobs
        }

        return render(request, 'works/list.html', context=t_list)
    
    return render(request, 'main_app/index.html')