from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Job,JobSeeker,Company,Provinces,Category


def landing(request):
    
    jobs = Job.objects.all()
    
    f_list= {
        "jobs": jobs
    }

    return render(request, 'works/landing.html', context=f_list)

def company(request):
    
    companies = Company.objects.all()
    
    f_list2= {
        "companies": companies
    }

    return render(request, 'works/companies.html', context=f_list2)



def home(request):
    return render(request, 'home.html')


def detail(request, job_name):
    if request.method == 'GET':
        try:
            jobs = Job.objects.get(title=job_name)
        except:
            jobs = None
        j_list = {
            'jobs' : jobs, 
            'flag' : False
        }
        return render(request, 'works/detail.html', context=j_list)
    if request.method == 'POST':
        current_job = Job.objects.get(title=job_name)
        description = request.POST['description']
        category = request.POST['category']
        location = request.POST['location']
        employer = request.POST['employer']
        created_at = request.POST['created_at']
        min_salary = request.post['min_salary']
        max_salary = request.post['max_salary']


        Job.objects.create(
            job = current_job,
            description = description,
            category = category,
            location = location,
            employer = employer,
            created_at = created_at,
            min_salary = min_salary,
            max_salary = max_salary
        )
        
        
        return render(request, 'works/detail.html', context=j_list)

