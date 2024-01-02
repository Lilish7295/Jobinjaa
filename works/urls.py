from django.urls import path
from .views import landing , detail , category , province

app_name = 'works'

urlpatterns = [
    path('', landing , name='jobs'),
    path("<str:id>" , detail , name='details'),
    path("home/" , landing , name='home'),  
]