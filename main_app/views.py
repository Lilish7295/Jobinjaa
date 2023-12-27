from django.shortcuts import render
from works.models import Job


def index(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        location = request.POST['location']
        
        jobs = Job.objects.filter(provinces_name=location,category_name=category,job_title=title)

        t_list ={
            'jobs' : jobs
        }

        return render(request, 'works/landing.html', context=t_list)
    
    return render(request, 'main_app/index.html')