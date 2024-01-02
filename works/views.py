from django.http import HttpResponse, JsonResponse
from works.models import Job,JobSeeker,Company,Provinces,Category
from django.shortcuts import render


def landing(request):
    jobs = Job.objects.all() 
    f_list= {
        "jobs": jobs
    } 
    return render(request, 'works/landing.html', context=f_list)


def detail(request,id):
    if request.method == 'GET':
        try:
            jobs = Job.objects.get(pk=id)
        except:
            jobs = None
        j_list = {
            'jobs' : jobs, 
            'flag' : False
        }
        return render(request, 'works/detail.html', context=j_list)
    

def category(request):
    categories = Category.objects.all() 
    c_list= {
        "categories": categories
    } 
    return render(request, 'works/navbar.html', context=c_list)


def province(request):
    provinces = Provinces.objects.all() 
    p_list= {
        "provinces": provinces
    } 
    return render(request, 'works/navbar.html', context=p_list)