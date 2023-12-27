from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Job,JobSeeker,Company,Provinces,Category
from django.shortcuts import render






def landing(request):
    
    jobs = Job.objects.all()
    
    f_list= {
        "jobs": jobs
    }

    return render(request, 'landing.html', context=f_list)

def company(request):
    
    companies = Company.objects.all()
    
    f_list2= {
        "companies": companies
    }

    return render(request, 'works/companies.html', context=f_list2)



def home(request):
    return render(request, "home.html")

