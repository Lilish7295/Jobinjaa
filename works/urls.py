from django.urls import path
from .views import landing , home

app_name = 'works'

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', landing, name='jobs'),
    

]