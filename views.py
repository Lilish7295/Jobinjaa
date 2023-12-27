from django.shortcuts import render,get_object_or_404
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






def job_detail(request, job_id):

    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

def generate_reservation_code():
    # this is a function to generate random unique reservation code
    random_code = random.randint(10000000,99999999)
    try:
        JobSeeker.objects.get(reservation_code=random_code)
        generate_reservation_code()
    except:
        return random_code


def detail(request, code):
    if request.method == 'GET':
        try:
            jobs = Job.objects.get(no=code)
        except:
            jobs = None
        f_list = {
            'jobs' : jobs, 
            'flag' : False
        }
        return render(request, 'job_detail.html', context=f_list)
    if request.method == 'POST':
        current_jobseeker = JobSeeker.objects.get(no=code)
        email=request.POST['email']
        name=request.POST['name']
        phone_number=request.POST['phone_number']
        birthday=request.POST['birthday']
        gender=request.POST['gender']
        # check available candidate
        if name == '':
            return HttpResponse('Error: Name should not be empty')
        if int(Job.candidate) <= 0:
            return HttpResponse("Error: There is no enough seat. max seat available is :{}".format(current_job.candidate))
        JobSeeker.objects.create(
            job=current_job,
            name=name,
            e=lastname,
            email = email,
            birthday=birthday,
            cv=cv,
            reservation_code=generate_reservation_code()
        )
        current_job.candidate = current_job.candidate - 1
        current_jobseeker.save()
        f_list = {
            'jobs' : current_job,
            'flag' : True
        }
        return render(request, 'job_detail.html', context=f_list)
        
