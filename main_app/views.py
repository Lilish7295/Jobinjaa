from django.shortcuts import render
from works.models import Flight


def index(request):
    if request.method == 'POST':
        origin = request.POST['origin']
        dest = request.POST['dest']
        date = request.POST['date']
        seat = request.POST['seat']
        flights = Flight.objects.filter(origin__city=origin, destination__city=dest)
        f_list ={
            'flights' : flights
        }
        return render(request, 'works/list.html', context=f_list)
    return render(request, 'main_app/index.html')