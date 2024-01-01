from django.http import HttpResponse, JsonResponse
from works.models import Job,JobSeeker,Company,Provinces,Category
from django.shortcuts import render


def landing(request):
    jobs = Job.objects.all() 
    f_list= {
        "jobs": jobs
    } 
    return render(request, 'works/landing.html', context=f_list)


def home(request):
    return render(request, "home.html")


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
        return render(request, 'detail.html', context=j_list)
    
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

